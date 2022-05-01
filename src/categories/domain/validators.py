# Python
from typing import Dict

# Third
from rest_framework import serializers

# Apps
from src.core.domain.validators import DRFValidator


class CategoryValidator(DRFValidator):

    def validate(self, serializer_class: serializers.Serializer, data: Dict) -> bool:
        rules = serializer_class(data=data if data is not None else {})
        return super().validate(rules)
