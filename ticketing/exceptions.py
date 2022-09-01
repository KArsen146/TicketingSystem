class TransactionException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(message, *args)


class IncorrectDataException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(message, *args)


class CreatingException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(message, *args)
