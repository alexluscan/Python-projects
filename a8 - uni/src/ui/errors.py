from datetime import datetime


class ValidationException(Exception):
    def __init__(self, error_msg):
        self._error_messages = error_msg

    @property
    def error_messages(self):
        return self._error_messages

    def __str__(self):
        return "Validation error:" + f"\n {self._error_messages}"


class BookError(ValidationException):
    def __init__(self, error_msgs  = "Error!"):
        ValidationException.__init__(self, error_msgs)

    def validate_id(self, id: str):
        if not id.isnumeric():
            raise ValidationException("Book's ID invalid!")

    def validate_string(self, name: str):
        names = name.split(" ")
        for name in names:
            if not name.isalpha():
                raise ValidationException("Invalid data!")


class ClientError(ValidationException):
    def __init__(self, error_msgs  = "Error!"):
        ValidationException.__init__(self, error_msgs)

    def validate_id(self, id: str):
        if not id.isnumeric():
            raise ValidationException("Client's ID invalid!")

    def validate_string(self, name: str):
        names = name.split(" ")
        for name in names:
            if not name.isalpha():
                raise ValidationException("String invalid!")


class RentalError(ValidationException):
    def __init__(self, error_msgs = "Error!"):
        ValidationException.__init__(self, error_msgs)

    def validate_id(self, id: str):
        if not id.isnumeric():
            raise ValidationException("Rental's ID invalid!")

    def validate_string(self, name: str):
        names = name.split(" ")
        for name in names:
            if not name.isalpha():
                raise ValidationException("String invalid!")

    def validate_date(self, date: str):
        date_str = date
        # Validate the entered date format
        if not datetime.strptime(date_str, "%Y-%m-%d"):
            raise ValidationException("Invalid date format. Please enter the date in the format 'YYYY-MM-DD'.")


class TypeError(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)