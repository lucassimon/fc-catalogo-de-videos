"""
A domain seedwork for validator Interfaces
"""

# Python
import abc
from typing import Any, Dict, List, Generic, TypeVar
from dataclasses import dataclass

# Third
from rest_framework import serializers

ErrorsField = Dict[str, List[str]]
PropsValidated = TypeVar("PropsValidated")


@dataclass(frozen=True)
class ValidatorFieldInterface(abc.ABC, Generic[PropsValidated]):
    """
    Interface for any Validator instance with a validate method
    """

    errors: ErrorsField = None
    validated_data: PropsValidated = None

    @abc.abstractmethod
    def validate(self, validator: Any):
        raise NotImplementedError()


class DRFValidator(ValidatorFieldInterface[PropsValidated]):
    """
    Interface para validação de serializers do django rest framework
    """

    def validate(self, validator: serializers.Serializer) -> bool:
        if not validator.is_valid():
            errors = {field: [str(_error) for _error in _errors] for field, _errors in validator.errors.items()}
            object.__setattr__(self, "errors", errors)
            return False

        data = dict(validator.validated_data)
        object.__setattr__(self, "validated_data", data)
        return True
