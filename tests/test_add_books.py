import pytest
from api.library_api_calls import add_book, get_books

def test_add_a_book():
    add_a_book_response = add_book("The Great Gatsby", "F. Scott Fitzgerald")
    assert add_a_book_response.title == "The Great Gatsby"
    assert add_a_book_response.author == "F. Scott Fitzgerald"
    assert add_a_book_response.is_borrowed == False

    get_books_response = get_books()
    assert add_a_book_response.id == get_books_response[-1].id
    assert get_books_response[-1].title == "The Great Gatsby"
    assert get_books_response[-1].author == "F. Scott Fitzgerald"

def test_add_a_book_wrong_format():
    with pytest.raises(Exception) as e:
        add_a_book_response = add_book("Name")

    assert e.type == TypeError
    assert str(e.value) == "add_book() missing 1 required positional argument: 'author'"