import pytest
from api.library_api_calls import return_book, get_users, borrow_book, get_books

@pytest.fixture
def setup_borrowed_book():
    users = get_users()
    user = next((user for user in users if len(user.borrowed_books) > 0), None)
    if user is None:
        books = get_books()
        borrow_book(users[0].id, books[0].id)

def test_return_book(setup_books_on_library, setup_borrowed_book):
    users = get_users()
    user = next((user for user in users if len(user.borrowed_books) > 0), None)
    borrowed_book_id = user.borrowed_books[0]
    response = return_book(user.id, borrowed_book_id)
    assert response['message'] == "Book returned successfully"
    users = get_users()
    user = next((user for user in users if user.id == user.id), None)
    assert borrowed_book_id not in user.borrowed_books
    books = get_books()
    book = next((book for book in books if book.id == borrowed_book_id), None)
    assert book.is_borrowed == False

test_return_error_data = [
    (100, 1, "User not found"),
    (1, 100, "Book not found"),
    (1, 1, "Book was not borrowed by the user")
]

@pytest.mark.parametrize("user_id, book_id, error_message", test_return_error_data)
def test_return_error(setup_books_on_library,setup_no_borrowed_books, user_id, book_id, error_message):
    with pytest.raises(Exception) as e:
        return_book(user_id, book_id)
    assert e.type == RuntimeError
    assert str(e.value) == error_message


