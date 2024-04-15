from src.repository.repository import Repository
from src.domain.idobject import IdObject
import os
import sys
import copy
from src.ui.errors import *
class Text(Repository):

    def __init__(self, filerep, classe, client_rep='', book_rep='') -> None:
        self.__file_name = filerep
        self.__class_rep = classe
        self.__clients_rep = client_rep
        self.__books_rep = book_rep
        super().__init__(filerep)
        self.__load_file()

    def add(self, object: IdObject):
        super().add(object)
        self.__save_file()
        return object

    def remove(self, object: IdObject):
        super().remove(object)
        self.__save_file()
        return object

    def __save_file(self):
        """Save file in text file folder
        """
        self.File_object = open(self.__file_name, "w")
        strings = ''
        for each in self._data:
            strings += self._data[each].get_items()
        self.File_object.write(strings)
        self.File_object.close()

    def __load_file(self):
        """Load file in text file folder

        Raises:
            RepositoryError: File not found.
            RepositoryError: Cannot start repository
        """
        try:
            if os.path.getsize(self.__file_name) > 0:
                strings = []
                line = ''

                with open(self.__file_name, "r") as file:
                    line = file.readlines()
                for each in line:
                    strings.append([])
                    line_splited = each.split(",")
                    for linespl in line_splited:
                        strings[-1].append(copy.deepcopy(linespl))
                for each in strings:
                    each[-1] = each[-1].replace("\n", ' ')
                    if self.__class_rep == 'Client':
                        object = getattr(sys.modules[__name__], self.__class_rep)(int(each[0]), each[1].strip())
                    elif self.__class_rep == 'Book':
                        object = getattr(sys.modules[__name__], self.__class_rep)(int(each[0]), each[1], each[0])
                    elif self.__class_rep == 'Rental':
                        client = self.__clients_rep.find(int(each[1]))
                        book = self.__books_rep.find(int(each[2]))
                        if client == None or book == None:
                            continue
                        object = getattr(sys.modules[__name__], self.__class_rep)(int(each[0]), client, book, each[3],
                                                                                  each[4])
                    self._data[object.id] = object
        except FileNotFoundError:
            raise ValidationException("File not found.")
        except OSError:
            raise ValidationException("Cannot start repository")
