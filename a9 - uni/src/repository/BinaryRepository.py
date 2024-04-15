from src.repository.repository import Repository
from src.domain.idobject import IdObject
import os
import pickle
from src.ui.errors import *


class Pickle(Repository):

    def __init__(self, filerep, classe, client_rep='', book_rep='') -> None:
        super().__init__(filerep)
        self.__file_name = filerep
        self.__load_file()

    def add(self, object: IdObject):
        super().add(object)
        self.__save_file()

    def remove(self, object: IdObject):
        super().remove(object)
        self.__save_file()

    def __save_file(self):
        """Save file in pickle folder
        """
        file = open(self.__file_name, "wb")
        pickle.dump(self._data, file)
        file.close()

    def __load_file(self):
        """Load file in pickle foler

        Raises:
            RepositoryError: File not found.
            RepositoryError: Cannot start repository
        """
        try:
            if os.path.getsize(self.__file_name) > 0:
                file = open(self.__file_name, "rb")
                self._data = pickle.load(file)
                file.close()
        except FileNotFoundError:
            raise ValidationException("File not found.")
        except OSError:
            raise ValidationException("Cannot start repository")