import pytest
from api.library_api_calls import get_users, borrow_book, get_books, add_book, return_book

@pytest.fixture
def setup_books_on_library():
    books = get_books()
    while len(books) < 2:
        add_book("Rich Dad Pour Dad", "Robert Kiyosaki")
        books = get_books()

def test_borrow_book(setup_books_on_library , setup_no_borrowed_books):
    first_user = get_users()[0]
    books = get_books()
    book = next((book for book in books if not book.is_borrowed), None)
    response = borrow_book(first_user.id, book.id)
    assert response['message'] == "Book borrowed successfully"
    books = get_books()
    book = next(book for book in books if book.id == book.id)
    assert book.is_borrowed == True
    users = get_users()
    user = next(user for user in users if user.id == first_user.id)
    assert book.id in user.borrowed_books

def test_borrow_book_already_borrowed(setup_books_on_library, setup_no_borrowed_books):
    first_user = get_users()[0]
    books = get_books()
    book = next((book for book in books if not book.is_borrowed), None)
    borrow_book(first_user.id, book.id)
    with pytest.raises(Exception) as e:
        borrow_book(first_user.id, book.id)
    assert e.type == RuntimeError
    assert str(e.value) == "Book already borrowed"

test_borrow_error_data = [
    (100, 1, "User not found"),
    (1, 100, "Book not found"),
]

@pytest.mark.parametrize("user_id, book_id, error_message", test_borrow_error_data)
def test_borrow_error(setup_books_on_library, setup_no_borrowed_books , user_id, book_id, error_message):
    with pytest.raises(Exception) as e:
        borrow_book(user_id, book_id)
    assert e.type == RuntimeError
    assert str(e.value) == error_message