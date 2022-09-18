import pytest

from django.contrib.auth.hashers import check_password

pytestmark = [pytest.mark.django_db]


def test_ok(as_user, user):
    result = as_user.get('/api/v1/users/me/')

    assert result['id'] == user.pk
    assert result['username'] == user.username
    assert result['firstName'] == user.first_name
    assert result['lastName'] == user.last_name
    assert result['surname'] == user.surname
    assert result['position'] == user.position
    assert result['rank'] == user.rank
    assert result['phone'] == user.phone


def test_update(as_user, user):
    as_user.patch('/api/v1/users/me/', data={
        'firstName': 'TEST',
        'lastName': 'TEST',
        'surname': 'TEST',
        'position': 'TEST',
        'rank': 'TEST',
        'phone': 'TEST',
        'password': 'TEST',
    })  # act

    user.refresh_from_db()
    assert user.first_name == 'TEST'
    assert user.last_name == 'TEST'
    assert user.surname == 'TEST'
    assert user.position == 'TEST'
    assert user.rank == 'TEST'
    assert user.phone == 'TEST'
    assert check_password('TEST', user.password)


def test_put_not_allowed(as_user):
    result = as_user.put('/api/v1/users/me/', as_response=True)

    assert result.status_code == 405


def test_anon(as_anon):
    result = as_anon.get('/api/v1/users/me/', as_response=True)

    assert result.status_code == 401
