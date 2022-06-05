from collections.abc import Iterable, Iterator
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    _reverse: bool = False

    def __init__(self, collection: list[Any], reverse: bool = False):
        self._collection = sorted(collection)
        self._reverse = reverse
        self._position = -1 if self._reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: list[Any]):
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def add(self, item: Any) -> None:
        self._collection.append(item)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, reverse=True)


if __name__ == '__main__':
    words = ["banana", "apple", "orange"]

    words_collection = WordsCollection(words)

    print("\n".join(words_collection))

    print()

    print("\n".join(words_collection.get_reverse_iterator()))
