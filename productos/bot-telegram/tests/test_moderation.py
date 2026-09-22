import unittest

from src.log import EventLogger
from src.moderation import Moderator


class _NullLogger:
    def log(self, event_type, data):
        pass


class TestModeration(unittest.TestCase):
    def setUp(self):
        self.config = {
            "rate_limit": {"messages": 2, "window_seconds": 10},
            "banned_phrases": ["airdrop gratis", "free money", "pump signal", "dm me"],
            "allowed_link_domains": ["github.com", "solana.com"],
            "warn_threshold": 3,
        }
        self.mod = Moderator(self.config, _NullLogger())

    def test_clean_message_ok(self):
        self.assertEqual(self.mod.check_message(1, 100, "hola grupo"), "ok")

    def test_banned_phrase_case_insensitive(self):
        self.assertEqual(self.mod.check_message(1, 100, "AIRDROP GRATIS ahora"), "warn")

    def test_disallowed_link(self):
        self.assertEqual(self.mod.check_message(1, 100, "mira https://evil.example.tld/x"), "warn")
        self.assertEqual(self.mod.check_message(1, 100, "repo https://github.com/nullforgedev"), "ok")

    def test_rate_limit(self):
        self.assertEqual(self.mod.check_message(1, 100, "uno"), "ok")
        self.assertEqual(self.mod.check_message(1, 100, "dos"), "ok")
        self.assertEqual(self.mod.check_message(1, 100, "tres"), "warn_ratelimit")

    def test_ban_after_threshold(self):
        self.mod.check_message(1, 100, "free money 1")
        self.mod.check_message(1, 100, "free money 2")
        self.assertEqual(self.mod.check_message(1, 100, "free money 3"), "ban")
        self.assertEqual(self.mod.check_message(1, 100, "hola"), "ban")


class TestLogger(unittest.TestCase):
    def test_log_writes_jsonl(self):
        import json
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "events.jsonl")
            logger = EventLogger(path)
            logger.log("test_event", {"chat": 1})
            with open(path, encoding="utf-8") as fh:
                line = json.loads(fh.readline())
            self.assertEqual(line["type"], "test_event")
            self.assertEqual(line["chat"], 1)
            self.assertIn("ts", line)


if __name__ == "__main__":
    unittest.main()