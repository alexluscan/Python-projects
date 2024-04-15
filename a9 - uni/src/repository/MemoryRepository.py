from src.repository.repository import Repository
from src.domain.idobject import IdObject
import os
import pickle
from src.ui.errors import *

class Memory:

    def __init__(self, filerep='', classe='', client_rep='', book_rep='') -> None:
        self._data = {}

    def add(self, object: IdObject):
        if not isinstance(object, IdObject):
            raise TypeError("Can only add IdObject instances")

        if object.id in self._data.keys():
            raise ValidationException("Already exists.")

        self._data[object.id] = object
        return object

    def remove(self, object: IdObject):
        if not isinstance(object, IdObject):
            raise TypeError("Can only delete IdObject instances")

        if not object.id in self._data.keys():
            raise ValidationException("This object doesen't exist.")
        del self._data[object.id]
        return object

    def __iter__(self):
        return RepositoryCounter(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def find(self, id: int):
        return self._data[id] if id in self._data.keys() else None

    @property
    def get_all(self):
        return self._data

class RepositoryCounter:
    def __init__(self, data: list):
        self._data = data
        self.__pos = -1

    def __next__(self):
        # return the next item we iterate over
        self.__pos += 1
        if self.__pos == len(self._data):
            raise StopIteration()
        return self._data[self.__pos]