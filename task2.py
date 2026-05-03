import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [b for b in self._books if b.title != title]

    def get_all_books(self) -> List[Book]:
        return self._books

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        new_book = Book(title, author, year)
        self.library.add_book(new_book)
        logger.info(f"Книга '{title}' додана.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f"Книга '{title}' видалена (якщо вона існувала).")

    def show_books(self) -> None:
        books = self.library.get_all_books()
        if not books:
            logger.info("Бібліотека порожня.")
        else:
            for book in books:
                logger.info(book)

def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()