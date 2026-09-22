import unittest

from src.faq import match_faq

ENTRIES = [
    {"keywords": ["qué es", "que es", "what is"], "answer": "Somos nullforge: tooling open-source para comunidades web3."},
    {"keywords": ["precio", "token", "price"], "answer": "Este es un grupo de builders, no de trading. Nada de señales acá."},
    {"keywords": ["roadmap"], "answer": "Roadmap público en el repo."},
]


class TestFaq(unittest.TestCase):
    def test_match_keyword(self):
        result = match_faq("buenas, ¿qué es este grupo?", ENTRIES)
        self.assertEqual(result, ENTRIES[0]["answer"])

    def test_match_spanish_no_accent(self):
        result = match_faq("a ver que es esto", ENTRIES)
        self.assertEqual(result, ENTRIES[0]["answer"])

    def test_match_price(self):
        result = match_faq("cual es el precio?", ENTRIES)
        self.assertEqual(result, ENTRIES[1]["answer"])

    def test_no_match(self):
        self.assertIsNone(match_faq("quien quiere jugar al futbol?", ENTRIES))


if __name__ == "__main__":
    unittest.main()