import json

import httpx


def match_faq(text, entries):
    low = text.lower()
    for entry in entries:
        for keyword in entry.get("keywords", []):
            if keyword.lower() in low:
                return entry["answer"]
    return None


class FaqHandler:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.entries = config.get("entries", [])
        self.use_llm = config.get("use_llm", False) and self.entries

    def answer(self, text):
        hit = match_faq(text, self.entries)
        if hit:
            return hit
        if self.use_llm:
            return self._ask_llm(text)
        return None

    def _ask_llm(self, text):
        llm = self.config.get("llm", {})
        payload = {
            "model": llm.get("model", "llama3.2"),
            "prompt": (
                "Sos el bot de una comunidad web3. Respondé en una o dos líneas "
                f"a esta pregunta de un miembro:\n{text}"
            ),
            "stream": False,
        }
        try:
            resp = httpx.post(llm.get("endpoint"), json=payload, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "").strip() or None
        except (httpx.HTTPError, json.JSONDecodeError, KeyError):
            self.logger.log("faq_llm_error", {"query": text})
            return None