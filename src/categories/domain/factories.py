# Apps
from src.categories.domain.validators import CategoryValidator


class CategoryValidatorFactory:
    @staticmethod
    def create():
        return CategoryValidator()
