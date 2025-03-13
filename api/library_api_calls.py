import requests
from models.models import Book, User

base_url = "http://127.0.0.1:5000"

def get_books():
    response = requests.get(f"{base_url}/books").json()
    books = [Book(**book) for book in response]
    return books

def add_book(title, author):
    response = requests.post(f"{base_url}/books", json={"title":title, "author":author}).json()
    book = Book(**response)
    return book

def delete_book(id):
    response = requests.delete(f"{base_url}/books/{id}").json()
    throw_server_exeption(response)
    return response

def update_book(id, title, author):
    response = requests.put(f"{base_url}/books/{id}", json={"title":title, "author":author}).json()
    throw_server_exeption(response)
    book = Book(**response)
    return book

def get_users():
    response = requests.get(f"{base_url}/users").json()
    users = [User(**user) for user in response]
    return users

def borrow_book(user_id, book_id):
    response = requests.post(f"{base_url}/users/{user_id}/borrow/{book_id}").json()
    throw_server_exeption(response)
    return response

def return_book(user_id, book_id):
    response = requests.post(f"{base_url}/users/{user_id}/return/{book_id}").json()
    throw_server_exeption(response)
    return response

def throw_server_exeption(response):
    if "error" in response:
        raise RuntimeError(response.get("error"))
