import abc
from dataclasses import dataclass
from typing import Any, Dict, List, TypeVar, Generic
from rest_framework import serializers

ErrorsField = Dict[str, List[str]]
PropsValidated = TypeVar('PropsValidated')

@dataclass(frozen=True)
class ValidatorFieldInterface(abc.ABC, Generic[PropsValidated]):
    errors: ErrorsField = None
    validated_data: PropsValidated = None

    @abc.abstractmethod
    def validate(self, validator: Any, data: Any):
        raise NotImplementedError()


class DRFValidator(ValidatorFieldInterface[PropsValidated]):

    def validate(self, serializer: serializers.Serializer) -> bool:
        if not serializer.is_valid():
            errors = {
                field: [str(_error) for _error in _errors]
                for field, _errors in serializer.errors.items()
            }
            object.__setattr__(self, 'errors', errors)
            return False
        else:
            data = dict(serializer.validated_data)
            object.__setattr__(self, 'validated_data', data)
            return True

