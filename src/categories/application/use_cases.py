# Apps
from src.categories.domain import entities


class CreateCategoryUseCase:

    def execute(self, input):

        entity = entities.Category(input)

        output = self.repository.insert(entity)

        return output

