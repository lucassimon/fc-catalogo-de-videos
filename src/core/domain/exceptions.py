# Apps
from src.core.domain.validators import ErrorsField


class InvalidUUIDException(Exception):
    def __init__(self, error: str = "Id must be a valid UUID") -> None:
        super().__init__(error)


class ValidationException(Exception):
    pass


class EntityValidationException(Exception):
    def __init__(self, error: ErrorsField) -> None:
        self.error = error
        super().__init__("Entity Validation Error")


class NotFoundException(Exception):
    pass
