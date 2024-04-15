from src.services.BookService import BookService


class Test:
    def __init__(self, repo):
        self.student_service = BookService(repo)

    def test_random_values(self):
        assert len(self.student_service.get_books_for_display()) == 10

    def test_add(self):
        self.student_service.add_book("1", "Ion", "Ana")
        assert len(self.student_service.get_books_for_display()) == 11

        self.student_service.add_book("2", "Ion", "Ana")
        assert len(self.student_service.get_books_for_display()) == 12

    def test_filter(self):
        self.student_service.add_book("1", "Ion", "Ana")
        self.student_service.filter_list("Ana")

        assert len(self.student_service.get_books_for_display()) == 10

    def test_undo(self):
        self.student_service.add_book("1", "Ion", "Ana")
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_books_for_display()) == 10

        self.student_service.add_book("2", "Ion", "* Ana")
        self.student_service.add_book("1", "Ion", "Ana")
        self.student_service.filter_list("*")
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_books_for_display()) == 12

    def test_all(self):
        self.test_random_values()
        self.test_add()
        self.test_filter()
        self.test_undo()
