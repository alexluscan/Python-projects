import pickle
import os
from src.repository.MemoryRepository import RepositoryError, Memory


class Binary(Memory):

    def __init__(self, file_name="books.data") -> None:
        self.__file_name = file_name
        super().__init__()
        self.__load_file()

    def add_book(self, list):
        super().add_book(list)
        self.__save_file()

    def undo_list(self):
        super().undo_list()
        self.__save_file()

    def __save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self.get_all(), file)
        file.close()

    def __load_file(self):
        try:
            if os.path.getsize(self.__file_name) > 0:
                file = open(self.__file_name, "rb")
                self._data = pickle.load(file)
                file.close()
        except FileNotFoundError:
            raise RepositoryError("File not found.")
        except OSError:
            raise RepositoryError("Cannot start repository")

    def modify_list2(self, new_list):
        super().modify_list(new_list)
        self.__save_file()
