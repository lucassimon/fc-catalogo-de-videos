from enum import unique
import pytest
from dataclasses import dataclass
from typing import List, Optional

from src.core.domain.entities import Entity
from src.core.domain.repositories import InMemorySearchableRepository, SearchParams, Filter

@dataclass(frozen=True, kw_only=True, slots=True)
class StubEntity(Entity):
    name: str
    price: int


class StubInMemorySearchableRepository(InMemorySearchableRepository[StubEntity, str]):
    sortable_fields: List[str] = ['name', 'price']

    def _apply_filter(self, items: List[StubEntity], filters: Optional[Filter]):
        if filters:
            items_filtered = filter(
                lambda item:
                filters.lower() in item.name.lower()
                or filters == str(item.price),
                items
            )
            return list(items_filtered)

        return items


def make_repo():
    return StubInMemorySearchableRepository()


@pytest.mark.unit
@pytest.mark.parametrize(
    "items, param, expected",
    [
        (   [StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271'
                ,name='test',
                price=100
            )],
            None,
            [StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='test',
                price=100
            )]
        ),
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='test',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='TEST',
                price=300
            ),
            StubEntity(name='fake', price=500)
        ], 'TEST', [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='test',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='TEST',
                price=300
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='test',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='TEST',
                price=300
            ),
            StubEntity(name='fake', price=500)
        ], '300', [
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='TEST',
                price=300
            ),
        ]),

    ],
)
def test_apply_filter(items, param, expected):
    repo = make_repo()
    result = repo._apply_filter(items, param)

    assert result == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "items, field_name, direction, expected",
    [
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
        ],
        'name',
        'asc',
        [
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ],
        'price',
        'asc',
        [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ],
        'name',
        'desc',
        [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ],
        'price',
        'desc',
        [
            StubEntity(
                unique_entity_id='7e8453bc-25f8-454a-9d79-d94d5acc32b7',
                name='a',
                price=300
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ]),
    ],
)
def test_apply_sort(items, field_name, direction, expected):
    repo = make_repo()
    result = repo._apply_sort(items, sort=field_name, sort_direction=direction)

    assert result == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "items, page, per_page, expected",
    [
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='a',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='c',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='d',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='e',
                price=100
            ),
        ],
        1,
        2,
        [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='a',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='a',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='c',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='d',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='e',
                price=100
            ),
        ],
        2,
        2,
        [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='c',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='d',
                price=100
            ),
        ]),
        ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='a',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='c',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='d',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='e',
                price=100
            ),
        ],
        3,
        2,
        [
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='e',
                price=100
            ),
        ]),
                ([
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='a',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='b',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='c',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='d',
                price=100
            ),
            StubEntity(
                unique_entity_id='dcc13d20-e91d-437d-a6ac-2fd60605a271',
                name='e',
                price=100
            ),
        ],
        4,
        2,
        [

        ]),
    ],
)
def test_apply_paginate(items, page, per_page, expected):
    repo = make_repo()
    result = repo._apply_paginate(items, page=page, per_page=per_page)

    assert result == expected
