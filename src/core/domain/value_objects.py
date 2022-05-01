# Python
import json
from abc import ABC
from dataclasses import fields, dataclass


@dataclass(frozen=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_names = [field.name for field in fields(self)]
        return (
            str(getattr(self, fields_names[0]))
            if len(fields_names) == 1
            else json.dumps({field_name: getattr(self, field_name) for field_name in fields_names})
        )
