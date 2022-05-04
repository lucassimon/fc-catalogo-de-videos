"""
Modulo seedwork para uma Entidade
"""

# Python
from abc import ABC
from dataclasses import field, asdict, dataclass

# Apps
from src.core.domain.unique_entity_id import UniqueEntityId


@dataclass(kw_only=True, frozen=True)
class Entity(ABC):
    """
    Classe Entidade
    """
    unique_entity_id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId())

    # pylint: disable=C0103
    @property
    def id(self):
        """
        Retorna o id do tipo UUID como string
        """
        return str(self.unique_entity_id)

    def to_dict(self):
        """
        Retorna um dicionario com o id como string
        """
        entity_dict = asdict(self)
        entity_dict.pop("unique_entity_id")
        entity_dict["id"] = self.id

        return entity_dict
