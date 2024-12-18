import json
from models.book import Book

class BookService:
    BOOKS_FILE = "storage/books.json"

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.BOOKS_FILE, "r") as f:
                return [Book.from_dict(book) for book in json.load(f)]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.BOOKS_FILE, "w") as f:
            json.dump([book.to_dict() for book in self.books], f)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        print(f"Book with ISBN {isbn} removed successfully!")

    def search_books(self, query):
        return [
            book.to_dict() for book in self.books
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == book.isbn
        ]
