import pytest
from typing import TYPE_CHECKING

from users.models import User

if TYPE_CHECKING:
    from app.testing.factory import FixtureFactory


@pytest.fixture
def user(factory: 'FixtureFactory') -> User:
    return factory.user(first_name='Петр', last_name='Возов', surname='Паровозович')
