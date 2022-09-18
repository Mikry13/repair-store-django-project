import pytest

pytestmark = [pytest.mark.django_db]


def test(user):
    result = user.full_name

    assert result == 'Возов Петр Паровозович'


def test_blank_surname(user):
    user.surname = ''

    result = user.full_name

    assert result == 'Возов Петр'
