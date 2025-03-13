import pytest
from api.library_api_calls import update_book, get_books

def test_update_book(setup_books_on_library):
    book_name = "Rich Dad Poor Dad"
    author = "Robert Kiyosaki"
    books = get_books()
    book = books[-1]
    book_id = book.id
    updated_book = update_book(book_id, book_name, author)
    assert updated_book.title == book_name
    assert updated_book.author == author
    books = get_books()
    assert books[-1].title == book_name
    assert books[-1].author == author
    assert books[-1].id == book_id

def test_update_book_wrong_format(setup_books_on_library):
    books = get_books()
    last_book = books[-1]
    with pytest.raises(Exception) as e:
        update_book(last_book.id)
    assert e.type == TypeError
    assert str(e.value) == "update_book() missing 2 required positional arguments: 'title' and 'author'"
    books = get_books()
    book = next((book for book in books if book.id == last_book.id), None)
    assert book is not None
    assert book.title == last_book.title
    assert book.author == last_book.author

def test_update_book_wrong_id(setup_books_on_library):
    books = get_books()
    last_book = books[-1]
    with pytest.raises(Exception) as e:
        response = update_book(100, "Rich Dad Poor Dad", "Robert Kiyosaki")
    assert e.type == RuntimeError
    assert str(e.value) == "Book not found"