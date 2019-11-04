import unittest
from translations import Translations


class TranslationsTest(unittest.TestCase):
    def test_translations(self):
        translations = Translations() \
            .add("screen1", "de-DE", "Titel", "Text") \
            .add("screen1", "en-GB", "Title", "Message")
        self.assertEqual(translations.get_title("any/path/with/de-DE/asdf", "screen1.png"), "Titel")
        self.assertEqual(translations.get_title("any/path/with/en-GB/asdf", "screen1.png"), "Title")
        self.assertEqual(translations.get_message("any/path/with/de-DE/asdf", "screen1.png"), "Text")
        self.assertEqual(translations.get_message("any/path/with/en-GB/asdf", "screen1.png"), "Message")

    def test_load_from_file(self):
        translations = Translations(filename="default.json")
        self.assertEqual(translations.get_title("any/path/with/en-GB/asdf", "screenshot.png"), "DEFAULT TRANSLATIONS")
        self.assertIsNone(translations.get_title("any/path/with/en-GB/asdf", "onlymessage.png"))


if __name__ == '__main__':
    unittest.main()
