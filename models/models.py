from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    is_borrowed: bool

@dataclass
class User:
    id: int
    name: str
    borrowed_books: list[Book]