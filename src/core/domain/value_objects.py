# Python
import json
import uuid
from abc import ABC
from dataclasses import dataclass, field, fields

# Apps
from src.core.domain.exceptions import InvalidUUIDException
from apps.core.utils import uuidv4


@dataclass(frozen=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_names = [field.name for field in fields(self)]
        return str(getattr(self, fields_names[0])) \
            if len(fields_names) == 1 \
            else json.dumps({ field_name: getattr(self, field_name) for field_name in fields_names })


@dataclass(frozen=True)
class UniqueEntityId:
    id: str = field(default_factory=lambda: uuidv4())

    def __post_init__(self):
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as exc:
            raise InvalidUUIDException() from exc

    def __str__(self):
        return f"{self.id}"
