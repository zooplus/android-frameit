"""
Translations used for the text on framed device screenshots
"""
import json
import os


class Translations(object):
    def __init__(self, filename=None):
        self._translations = {}
        if filename:
            for name in (os.path.join("translations", filename), filename):
                try:
                    with open(name) as f:
                        self._translations = json.load(f)
                        break
                except FileNotFoundError:
                    pass

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
                    if f"/{language}/" in path + "/" or f"/{language}_" in path:
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
