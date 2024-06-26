from src.repository.repository_exception import RepositoryException


class RentalRepository:
    def __init__(self):
        self.__rentals = []

    def add(self, rental, books, clients):
        # check if rental already exists
        if rental in self.__rentals:
            raise RepositoryException("Rental already exists!")

        # check if book exist
        if books is not None and not any(book.id == rental.book_id for book in books):
            raise RepositoryException(f"Book with ID {rental.book_id} does not exist!")

        # check if client exists
        if clients is not None and not any(
            client.id == rental.client_id for client in clients
        ):
            raise RepositoryException(
                f"Client with ID {rental.client_id} does not exist!"
            )

        for checked_rental in self.__rentals:
            if checked_rental.book_id == rental.book_id:
                # check if the book is alreay rented and not returned
                if checked_rental.returned_date is None:
                    raise RepositoryException(
                        f"Book with ID {rental.book_id} is already rented!"
                    )
                # check if the new rental date is after the last returned date
                elif rental.rented_date <= checked_rental.returned_date:
                    raise RepositoryException(
                        f"Book with ID {rental.book_id} cannot be rented before its last return date!"
                    )

        self.__rentals.append(rental)

    def get_all(self):
        return self.__rentals

    def update(self, rental):
        if rental not in self.__rentals:
            raise RepositoryException("Rental does not exist!")

        # see if returned date is valid
        if (
            rental.returned_date is not None
            and rental.returned_date <= rental.rented_date
        ):
            raise RepositoryException("Returned date must be after the rented date!")

        for index in range(len(self.__rentals)):
            if self.__rentals[index] == rental:
                self.__rentals[index] = rental
                break

    def get_rental_by_id(self, rental_id):
        for rental in self.__rentals:
            if rental.id == rental_id:
                return rental
        raise RepositoryException("Rental does not exist!")