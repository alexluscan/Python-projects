from src.services.BookService import *
import os


class UI:

    def __init__(self, rep):
        self.__rep = rep
        self.__service = BookService(self.__rep)
        self.__checks = VerifyInput(self.__service)

    def print_menu(self):
        print("1. Add a book.")
        print("2. Display the list of books.")
        print("3. Filter the book! Book titles starting with a given word are deleted from the list ")
        print("4. Undo the last operation that modified program data.")
        print("5. Exit")


    def print_ui(self):
        while True:
            self.print_menu()
            option = int(input("Choose option: "))
            if option == 1:
                input_isbn = input("isbn: ")
                input_author = input("author: ")
                input_title = input("title: ")
                try:
                    self.__checks.verify_add(input_isbn)
                    self.__service.add_book(input_isbn, input_author, input_title)
                except ValueError as ve:
                    print(ve)
            elif option == 2:
                try:
                    self.__checks.verify_display()
                    self.display_list_of_books()
                except ValueError as ve:
                    print(ve)
            elif option == 3:
                input_title = input("Type title for delete: ").strip()
                try:
                    self.__checks.verify_filter(input_title)
                    self.__service.filter_list(input_title)
                except ValueError as ve:
                    print(ve)
            elif option == 4:
                try:
                    self.__checks.verify_undo()
                    self.__service.undo_last_operation()
                except ValueError as ve:
                    print(ve)
            else:
                print("Good Bye!")
                break

    def display_list_of_books(self):
        books = self.__service.get_books_for_display()
        for book in books:
            print(book)