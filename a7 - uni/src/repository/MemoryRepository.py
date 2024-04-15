import copy


class RepositoryError(Exception):
    @property
    def message(self) -> str:
        return self.__message

    def __init__(self, message: str = "Not specified Repository Error"):
        self.__message = message

    def __str__(self) -> str:
        return self.__message


class Memory:

    def __init__(self) -> None:
        self._data = [[]]

    def add_book(self, listof):
        new_list = copy.deepcopy(self._data[-1])
        new_list.append(listof)
        self._data.append(new_list)
        return self._data

    def get_all(self):
        return self._data

    def get_books(self):
        return self._data[-1]

    def undo_list(self):
        self._data.pop()
        return self._data

    def modify_list(self, new_list):
        self._data.append(new_list)
        return self._data

    def length_of(self):
        return len(self._data)