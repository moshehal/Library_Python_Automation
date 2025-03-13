import pytest
from api.library_api_calls import get_books, delete_book

def test_get_books(setup_books_on_library):
    books = get_books()
    assert len(books) > 0
    assert isinstance(books[0].id, int)
    assert isinstance(books[0].title, str)
    assert isinstance(books[0].author, str)
    assert isinstance(books[0].is_borrowed, bool)

def test_get_books_empty(setup_books_on_library):
    get_books_response = get_books()
    for book in get_books_response:
        delete_book(book.id)
    books = get_books()
    print (books)
    assert len(books) == 0

def test_get_books_wrong_format(setup_books_on_library):
    with pytest.raises(Exception) as e:
        get_books_response = get_books(1)

    assert e.type == TypeError
    assert str(e.value) == "get_books() takes 0 positional arguments but 1 was given"