class Book:
    def __init__(self, isbn, author, title):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    @property
    def get_isbn(self):
        return self.__isbn

    @property
    def get_author(self):
        return self.__author

    @property
    def get_title(self):
        return self.__title

    def __str__(self):
        return str(self.get_isbn) + " " + self.get_author + " " + str(self.get_title)

    def serialize(self):
        return {"isbn": self.__isbn,
                "author": self.__author,
                "title": self.__title}