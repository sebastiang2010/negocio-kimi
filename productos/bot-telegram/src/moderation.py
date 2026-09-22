import re
import time
from collections import defaultdict
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s<>]+|www\.[^\s<>]+")


class RateLimiter:
    def __init__(self, max_messages, window_seconds):
        self.max_messages = max_messages
        self.window_seconds = window_seconds
        self._events = defaultdict(list)

    def record(self, chat_id, user_id):
        self._events[(chat_id, user_id)].append(time.time())

    def check(self, chat_id, user_id):
        key = (chat_id, user_id)
        now = time.time()
        recent = [t for t in self._events[key] if now - t < self.window_seconds]
        self._events[key] = recent
        return len(recent) > self.max_messages


class Moderator:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.rate_limiter = RateLimiter(
            config["rate_limit"]["messages"],
            config["rate_limit"]["window_seconds"],
        )
        self.banned_phrases = [p.lower() for p in config["banned_phrases"]]
        self.allowed_domains = set(config["allowed_link_domains"])
        self.warn_threshold = config["warn_threshold"]
        self._warns = defaultdict(int)
        self._banned = set()
        self._recently_warned = set()

    def check_message(self, chat_id, user_id, text):
        self.rate_limiter.record(chat_id, user_id)
        if user_id in self._banned:
            return "ban"
        low = text.lower()
        for phrase in self.banned_phrases:
            if phrase in low:
                return self._warn(chat_id, user_id)
        domains = self._extract_domains(text)
        if domains and not domains.issubset(self.allowed_domains):
            return self._warn(chat_id, user_id)
        if self.rate_limiter.check(chat_id, user_id):
            self._warns[user_id] += 1
            return "warn_ratelimit"
        return "ok"

    def _warn(self, chat_id, user_id):
        self._warns[user_id] += 1
        if self._warns[user_id] >= self.warn_threshold:
            self._banned.add(user_id)
            return "ban"
        return "warn"

    def recently_warned(self, user_id):
        return user_id in self._recently_warned

    def mark_warned(self, user_id):
        self._recently_warned.add(user_id)

    @staticmethod
    def _extract_domains(text):
        found = set()
        for match in URL_RE.findall(text):
            url = match if match.startswith("http") else f"http://{match}"
            host = urlparse(url).netloc.lower()
            if host.startswith("www."):
                host = host[4:]
            if host:
                found.add(host)
        return found