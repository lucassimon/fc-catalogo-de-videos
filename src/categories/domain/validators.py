"""
Define um ou mais validators para categoria
"""

# Python
from typing import Dict

# Third
from rest_framework import serializers

# Apps
from src.core.domain.validators import DRFValidator


class CategoryValidator(DRFValidator):
    """
    Classe para validar uma categoria utilizando o serialier do DRF
    """

    def check(self, serializer_class: serializers.Serializer, data: Dict) -> bool:
        """
        Metodo para validar
        """
        rules = serializer_class(data=data if data is not None else {})
        return super().validate(rules)
