import pytest
import uuid
from dataclasses import is_dataclass, FrozenInstanceError
from unittest.mock import patch

from src.core.domain import value_objects
from src.core.domain import exceptions
from apps.core import utils

@pytest.mark.unit
def test_unique_entity_uuid_is_a_dataclass():
    assert is_dataclass(value_objects.UniqueEntityId) is True

@pytest.mark.unit
def test_raises_an_exception_when_uuid_is_invalid():
    with patch.object(
        value_objects.UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=value_objects.UniqueEntityId._UniqueEntityId__validate
    ) as mock_validate:
        with pytest.raises(exceptions.InvalidUUIDException) as assert_error:
            value_objects.UniqueEntityId('invalid id')

        mock_validate.assert_called_once()

        assert assert_error.value.args[0] == 'Id must be a valid UUID'


@pytest.mark.unit
def test_valid_uuid_as_string():
    with patch.object(
        value_objects.UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=value_objects.UniqueEntityId._UniqueEntityId__validate
    ) as mock_validate:
        uuid = 'dcc13d20-e91d-437d-a6ac-2fd60605a271'
        obj = value_objects.UniqueEntityId(uuid)
        mock_validate.assert_called_once()
        assert obj.id == str(uuid)

@pytest.mark.unit
def test_valid_uuid_as_uuid_generated():
    with patch.object(
        value_objects.UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=value_objects.UniqueEntityId._UniqueEntityId__validate
    ) as mock_validate:
        uuid = utils.uuidv4()
        obj = value_objects.UniqueEntityId(uuid)
        mock_validate.assert_called_once()
        assert obj.id == str(uuid)


@pytest.mark.unit
def test_uuid_generated_when_default_params():
    with patch.object(
        value_objects.UniqueEntityId,
        '_UniqueEntityId__validate',
        autospec=True,
        side_effect=value_objects.UniqueEntityId._UniqueEntityId__validate
    ) as mock_validate:
        obj = value_objects.UniqueEntityId()
        uuid.UUID(obj.id)
        mock_validate.assert_called_once()


@pytest.mark.unit
def test_is_immutable():
    obj = value_objects.UniqueEntityId()
    with pytest.raises(FrozenInstanceError):
        obj.id = 'set another id'

@pytest.mark.unit
def test_dunder_str():
    uuid = utils.uuidv4()
    obj = value_objects.UniqueEntityId(uuid)

    assert obj.__str__() == str(uuid)
