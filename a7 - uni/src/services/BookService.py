import random
from src.domain.book import Book
import sys


class BookService:

    def __init__(self, rep):
        self.rep = rep
        self.generate_random_values()

    def add_book(self, isbn, author, title):
        self.rep.add_book(Book(isbn, author, title))

    def generate_random_values(self):
        self.add_book("978-3-16-000000-0", "Jules Verne", "Around the World in Eighty Days")
        self.add_book("978-3-16-000001-0", "Jules Verne", "The 20000 Leagues Under the Seas")
        self.add_book("978-3-16-000002-0", "Jules Verne", "Journey to the Center of the Earth")
        self.add_book("978-3-16-000003-0", "Ion Creanga", "The Harap-Alb Story")
        self.add_book("978-3-16-000004-0", "Ion Creanga", "Childhood Memories")
        self.add_book("978-3-16-000005-0", "Ion Creanga", "The bag with two coins")
        self.add_book("978-3-16-000006-0", "William Shakespeare", "The Hamlet")
        self.add_book("978-3-16-000007-0", "William Shakespeare", "Romeo and Julieta")
        self.add_book("978-3-16-000008-0", "William Shakespeare", "Julius Caesar")
        self.add_book("978-3-16-000009-0", "Robert Martin", "The Clean Code")

    def filter_list(self, title_for_delete):
        books = self.rep.get_books()
        new_books = []
        for i in range(len(books)):
            title = books[i].get_title
            title = title.split()
            if title[0].lower() != title_for_delete.lower():
                new_books.append(books[i])
        self.rep.modify_list(new_books)

    def undo_last_operation(self):
        self.rep.undo_list()

    def get_books_for_display(self):
        return self.rep.get_books()


class VerifyInput:

    def __init__(self, logic_input) -> None:
        self.logic = logic_input

    def verify_add(self, isbn_verify):
        books = self.logic.rep.get_books()
        for book in books:
            if book.get_isbn.lower() == isbn_verify.lower():
                raise ValueError("isbn already added")

    def verify_display(self):
        books = self.logic.rep.get_books()
        if len(books) == 0:
            raise ValueError("List is empty!")

    def verify_filter(self, input_title):
        books = self.logic.rep.get_books()
        if len(books) == 0:
            raise ValueError("List is empty!")
        if len(input_title.split()) != 1:
            raise ValueError("Type only one word for filter.")

    def verify_undo(self):
        books = self.logic.rep.length_of()
        if books == 1:
            raise ValueError("List is empty!")
