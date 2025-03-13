import pytest
from api.library_api_calls import delete_book, get_books

def test_delete_book(setup_books_on_library):
    books = get_books()
    last_book = books[-1]
    response = delete_book(last_book.id)
    assert response['message'] == "Book deleted"
    books = get_books()
    book = next((book for book in books if book.id == last_book.id), None)
    assert book is None

def test_delete_not_found_book(setup_books_on_library):
    with pytest.raises(Exception) as e:
        response = delete_book(100)
    assert e.type == RuntimeError
    assert str(e.value) == "Book not found"