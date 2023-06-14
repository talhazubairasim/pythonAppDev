import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_english_to_french(self):
        english_text = 'Hi'
        expected_french_text = 'Bonjour'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_french_to_english(self):
        # Test translation of 'Bonjour' to English
        french_text = 'Bonjour'
        expected_english_text = 'Hello'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)


if __name__ == '__main__':
    unittest.main()
