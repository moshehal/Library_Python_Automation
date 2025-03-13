import pytest
from api.library_api_calls import get_users

def test_get_users():
    users = get_users()
    assert len(users) > 0
    assert isinstance(users[0].id, int)
    assert isinstance(users[0].name, str)
    assert isinstance(users[0].borrowed_books, list)
