import os
import copy
import json
import mysql.connector

# from src.repository.repository import RepositoryError, Repository
from src.repository.MemoryRepository import RepositoryError, Memory
from src.domain.book import *


class JSON(Memory):

    def __init__(self, file_name = "book.json") -> None:
        """JSON init for Repository

        Args:
            file_name (_type_): file name for saving
        """
        self.__file_name = file_name
        super().__init__()
        self.__load_file()

    def add_book(self, listof):
        """Adding book and saving

        Args:
            list (_type_): id class to be saved
        """
        super().add_book(listof)
        self.__save_file()

    def undo_list(self):
        """Undo list and saving in file
        """
        super().undo_list()
        self.__save_file()

    def modify_list(self, new_list):
        """Modify list and savinf

        Args:
            new_list (list): new list for modify
        """
        super().modify_list(new_list)
        self.__save_file()

    def __save_file(self):
        """Save file in JSON folder
        """
        json_data = []
        for each in self._data[-1]:
            json_data.append(each.serialize())
        with open(self.__file_name, "w") as outfile:
            json.dump(json_data, outfile)

    def __load_file(self):
        """Load file in JSON foler

        Raises:
            RepositoryError: File not found.
            RepositoryError: Cannot start repository
        """
        try:
            if os.path.getsize(self.__file_name) > 0:
                file = open(self.__file_name)
                line = json.load(file)
                books = []
                for each in line:
                    line_splited = each
                    books.append(
                        [copy.deepcopy(line_splited["isbn"].strip()), copy.deepcopy(line_splited["author"].strip()),
                         copy.deepcopy(line_splited["title"].strip())])
                self._data.append([])
                for each in books:
                    self._data[-1].append(Book(each[0], each[1], each[2]))
                file.close()
        except FileNotFoundError:
            raise RepositoryError("File not found.")
        except OSError:
            raise RepositoryError("Cannot start repository")


class MYSQL(Memory):

    def __init__(self, filename="") -> None:
        super().__init__()
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="Voda",
            password="root",
            database="books"
        )
        self.__mycursor = self.__mydb.cursor()
        self.__load_db()

    def add_book(self, listof):
        """Adding book and saving

        Args:
            list (_type_): id class to be saved
        """
        super().add_book(listof)
        self.__add_in_db(listof)

    def undo_list(self):
        """Undo list and saving in file
        """
        super().undo_list()
        self.__save_db()

    def modify_list(self, new_list):
        """Modify list and savinf

        Args:
            new_list (list): new list for modify
        """
        super().modify_list(new_list)
        self.__modify_db(new_list)

    def __modify_db(self, newlist: list):
        self.__mycursor.execute("SELECT isbn FROM book_list")
        isbn_list = self.__mycursor.fetchall()
        for each in isbn_list:
            exist_in_newlist = False
            for book in self._data[-1]:
                if book.getisbn == each[0]:
                    exist_in_newlist = True
            if not exist_in_newlist:
                self.__mycursor.execute("DELETE FROM book_list WHERE isbn = %s", (each[0],))
                self.__mydb.commit()
        pass

    def __save_db(self):
        """Save file in JSON folder
        """
        self.__mycursor.execute("TRUNCATE TABLE book_list")
        for each in self._data[-1]:
            self.__add_in_db(each)

    def __add_in_db(self, idclass):
        self.__mycursor.execute(f"INSERT INTO book_list VALUES (%s,%s,%s)",
                                (f"{idclass.get_isbn}", f"{idclass.get_author}", f"{idclass.get_title}"))
        self.__mydb.commit()

    def __load_db(self):
        """Load file in JSON foler

        Raises:
            RepositoryError: File not found.
            RepositoryError: Cannot start repository
        """
        try:
            self.__mycursor.execute("SELECT * FROM book_list")
            myresult = self.__mycursor.fetchall()
            for each in myresult:
                self._data[-1].append(Book(each[0], each[1], each[2]))
        except FileNotFoundError:
            raise RepositoryError("File not found.")
        except OSError:
            raise RepositoryError("Cannot start repository")