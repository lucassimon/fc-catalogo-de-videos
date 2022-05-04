"""
Define factories para o dominio Category
"""
# Apps
from src.categories.domain.validators import CategoryValidator


class CategoryValidatorFactory:
    """
    Representa uma factory pattern para criar um validator
    """

    @staticmethod
    def create():
        """
        Instancia uma classe do tipo Validator
        """
        return CategoryValidator()
