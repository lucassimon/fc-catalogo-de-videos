class InvalidUUIDException(Exception):
    def __init__(self, error: str = 'Id must be a valid UUID') -> None:
        super().__init__(error)
