from src.domain.book import Book
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDBRepository:

    def _init_(self):

        # Initialize MongoDB Connection
        self.client = MongoClient("mongodb+srv://alexluscan:<password>@cluster0.y5pg3om.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        # Initialize Current Data
        self.__history = []
        self.__data = []
        self.db = self.client['library']
        self.collection = self.db['books']

        # Initialize history collection
        self.history_collection = self.db['book_history']

    # DataBase Management
    def __update_database_history(self, operation, document):
        """
        Update Memory History by appending current memory
        :return: N/A
        """

        # Maintain a log of operations and documents for "undo"
        self.__history.append({"operation": operation, "document": document})

    def get_by_isbn(self, given_isbn: str):
        """
        Find and return a book in current memory by ISBN
        :param given_isbn: ISBN we are looking for
        :return: ValueError if no book with given ISBN was found
        """

        book = self.collection.find_one({"isbn": given_isbn})
        if book:
            return book
        else:
            raise ValueError("Book Not Found!")

    def get_all(self) -> list:
        """
        :return: A list of all books in current memory
        """

        book_list = []
        for book_dict in self.collection.find():
            book_list.append(Book(book_dict["isbn"], book_dict["author"], book_dict["title"]))
        return book_list

    # Task Operations
    def add_book(self, listof):
        """Function for add book with id of Class

        Args:
            listof (id): id of class to be added in list

        Returns:
            list: list with all data
        """
        new_list = copy.deepcopy(self._data[-1])
        new_list.append(listof)
        self._data.append(new_list)
        return self._data

    def remove(self, to_remove: list):
        """
        Remove given book from database
        :param to_remove: Book instances to remove
        :return: N/A
        """

        deleted_books = []
        for book in to_remove:
            self.collection.delete_one({"isbn": book.isbn})
            deleted_books.append({"isbn": book.isbn, "author": book.author, "title": book.title})
        self.__update_database_history("remove", deleted_books)

    def undo(self):
        """
        Reverts the last action by applying reverse operation
        :return: N/A
        """

        if self.__history:
            last_action = self.__history.pop()
            operation = last_action["operation"]
            document = last_action["document"]

            if operation == "add":

                # Undo addition by removing the document
                self.collection.delete_one({"isbn": document["isbn"]})
            elif operation == "remove":

                # Undo removal by adding the document back
                for book in document:
                    self.collection.insert_one(book)
            else:
                raise ValueError("Unknown operation type in history log.")

        else:
            raise ValueError("No history available for undo.")

    def close_connection(self):
        self.client.close()