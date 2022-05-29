from abc import ABC, abstractmethod


class LanguageLocalizer(ABC):  # General interface
    @abstractmethod
    def localize(self, msg: str) -> str:   # General (factory) method
        pass


class EnglishLocalizer(LanguageLocalizer):
    def localize(self, msg: str) -> str:
        return msg


class FrenchLocalizer(LanguageLocalizer):
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


class SpanishLocalizer(LanguageLocalizer):
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


if __name__ == '__main__':
    el = EnglishLocalizer()
    fl = FrenchLocalizer()
    sl = SpanishLocalizer()

    word_list = ["car", "cycle", "bicycle"]

    print("English localizations: " + ", ".join([el.localize(word) for word in word_list]))
    print("French localizations: " + ", ".join([fl.localize(word) for word in word_list]))
    print("Spanish localizations: " + ", ".join([sl.localize(word) for word in word_list]))
