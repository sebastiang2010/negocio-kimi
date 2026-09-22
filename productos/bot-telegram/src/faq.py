"""FAQ: matching por keywords + fallback opcional a LLM local (Ollama)."""

from __future__ import annotations

import json
import urllib.request


class FaqEngine:
    def __init__(self, cfg: dict):
        self.enabled = cfg.get("enabled", True)
        self.entries = cfg.get("entries", [])
        self.use_llm = cfg.get("use_llm", False)
        self.ollama_url = cfg.get("ollama_url", "http://localhost:11434").rstrip("/")
        self.ollama_model = cfg.get("ollama_model", "llama3.1:8b")

    def match(self, text: str) -> str | None:
        """Devuelve respuesta por keywords, o None si no hay match."""
        low = text.lower()
        for entry in self.entries:
            if any(k.lower() in low for k in entry.get("keywords", [])):
                return entry["answer"]
        return None

    def answer(self, text: str) -> str | None:
        """Keyword match primero; si no hay, LLM opcional con contexto."""
        if not self.enabled:
            return None
        hit = self.match(text)
        if hit:
            return hit
        if self.use_llm:
            return self._llm_answer(text)
        return None

    def _llm_answer(self, question: str) -> str | None:
        knowledge = "\n".join(
            f"- P: {', '.join(e.get('keywords', []))} -> {e['answer']}"
            for e in self.entries
        )
        prompt = (
            "Eres el moderador de un grupo de Telegram tecnico. Responde breve, "
            "directo y sin hype, usando SOLO la informacion de esta base de "
            "conocimiento. Si no sabes, di que un admin va a responder.\n\n"
            f"Base de conocimiento:\n{knowledge}\n\n"
            f"Pregunta del usuario: {question}\nRespuesta:"
        )
        try:
            req = urllib.request.Request(
                f"{self.ollama_url}/api/generate",
                data=json.dumps(
                    {"model": self.ollama_model, "prompt": prompt, "stream": False}
                ).encode(),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read()).get("response", "").strip() or None
        except Exception:
            return None
