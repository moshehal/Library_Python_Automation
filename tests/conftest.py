import pytest
from api.library_api_calls import *

@pytest.fixture
def setup_books_on_library():
    books = get_books()
    if len(books) == 0:
        add_book("The Great Gatsby", "F. Scott Fitzgerald")

@pytest.fixture
def setup_no_borrowed_books():
    users = get_users()
    for user in users:
        if len(user.borrowed_books) > 0:
            for book_id in user.borrowed_books:
                return_book(user.id, book_id)