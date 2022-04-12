# Python
from abc import ABC
from dataclasses import asdict, dataclass, field

# Apps
from apps.core.value_objects import UniqueEntityId


@dataclass(kw_only=True, frozen=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId())

    @property
    def id(self):
        return str(self.unique_entity_id)

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict["id"] = self.id

        return entity_dict
