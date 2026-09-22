"""Moderacion anti-spam: rate limiting, frases prohibidas, control de links."""

from __future__ import annotations

import time
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass
class Verdict:
    is_spam: bool = False
    reason: str = ""


@dataclass
class Moderator:
    cfg: dict
    warns: dict[int, int] = field(default_factory=lambda: defaultdict(int))
    _msg_times: dict = field(default_factory=lambda: defaultdict(deque))

    def check(self, user_id: int, text: str, is_admin: bool) -> Verdict:
        if is_admin:
            return Verdict()
        verdict = self._rate_limit(user_id)
        if verdict.is_spam:
            return verdict
        if text:
            verdict = (self._banned_phrases(text) or self._links(text)
                       or Verdict())
        return verdict

    def _rate_limit(self, user_id: int) -> Verdict:
        window = self.cfg.get("rate_limit_window_sec", 10)
        limit = self.cfg.get("rate_limit_messages", 5)
        now = time.monotonic()
        q = self._msg_times[user_id]
        while q and now - q[0] > window:
            q.popleft()
        q.append(now)
        if len(q) > limit:
            return Verdict(True, f"rate_limit ({len(q)} msgs en {window}s)")
        return Verdict()

    def _banned_phrases(self, text: str) -> Verdict | None:
        low = text.lower()
        for phrase in self.cfg.get("banned_phrases", []):
            if phrase.lower() in low:
                return Verdict(True, f"frase prohibida: '{phrase}'")
        return None

    def _links(self, text: str) -> Verdict | None:
        allowed = self.cfg.get("allowed_link_domains", [])
        words = text.split()
        for w in words:
            if "http://" in w or "https://" in w:
                if not any(d in w for d in allowed):
                    return Verdict(True, "link no permitido")
        return None

    # --- acciones -----------------------------------------------------

    def add_warn(self, user_id: int) -> tuple[int, bool]:
        """Suma warn; devuelve (total, debe_banear)."""
        self.warns[user_id] += 1
        threshold = self.cfg.get("warn_threshold", 3)
        return self.warns[user_id], self.warns[user_id] >= threshold
