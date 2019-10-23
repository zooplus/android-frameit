"""
Translations used for the text on framed device screenshots
"""


class Translations(object):
    def __init__(self):
        self._translations = {}

    def add(self, filename_part, language, title, message):
        """
        Add a translation for given screen and language
        :param filename_part: A part of the filename which identifies the right screenshot file, for example "screen_1"
        :param language: language as used in the folder name, for example "de-DE"
        :param title: localized title to show
        :param message: localized message to show below the title
        :return: self
        """
        if filename_part not in self._translations:
            self._translations[filename_part] = {
                language: {
                    "title": title,
                    "message": message
                }
            }
        else:
            self._translations[filename_part][language] = {
                "title": title,
                "message": message
            }
        return self

    def _get_translations(self, path, filename, key):
        for filename_part in self._translations:
            if filename_part in filename:
                for language in self._translations[filename_part]:
                    if f"/{language}/" in path:
                        d = self._translations[filename_part][language]
                        if d:
                            return d[key]

    def get_title(self, path, filename):
        """
        :param path: path to the screenshot which includes the language as one element
        :param filename: filename of the screenshot
        :return: the title to show for given path and filename
        """
        return self._get_translations(path, filename, "title")

    def get_message(self, path, filename):
        """
        :param path: path to the screenshot which includes the language as one element
        :param filename: filename of the screenshot
        :return: the message to show for given path and filename
        """
        return self._get_translations(path, filename, "message")


def create():
    return Translations() \
            .add("screen_1", "de-DE", "20 JAHRE ZOOPLUS",
                 "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern") \
            .add("screen_3", "de-DE", "IHRE GESPEICHERTEN PRODUKTE",
                 "Schnell und einfach\nIhre Lieblingsprodukte wiederfinden") \
            .add("screen_7", "de-DE", "ALLES AUF EINEN BLICK",
                 "Übersichtliche und detaillierte Informationen\nzu all unseren Produkten") \
            .add("screen_2", "de-DE", "EINFACH WIEDERBESTELLEN",
                 "In wenigen Sekunden Ihre bereits\ngekauften Produkte nochmals bestellen") \
            .add("screen_1", "en-GB", "WELCOME",
                 "Pick your pet's favorite products\nout of more than 8.000 items") \
            .add("screen_3", "en-GB", "YOUR SAVED PRODUCTS",
                 "Access your favorite products easily") \
            .add("screen_7", "en-GB", "EVERYTHING AT A GLANCE",
                 "Detailed information to all of our products") \
            .add("screen_2", "en-GB", "REORDER EASILY",
                 "Reorder products with a few simple taps")
