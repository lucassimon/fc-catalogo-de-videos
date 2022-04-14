from typing import Any

from rest_framework import serializers

from src.core.domain.validators import DRFValidator

class CategoryValidator(DRFValidator):

    def validate(self, serializer_class: serializers.Serializer, data: Any) -> bool:
        rules = serializer_class(data=data)
        return super().validate(rules)
