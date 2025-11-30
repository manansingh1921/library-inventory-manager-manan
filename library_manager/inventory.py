import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.data_file = Path("data/library.json")
        self.data_file.parent.mkdir(exist_ok=True)
        self.load()
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save()
        print(f"Added: {book}")
    
    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]
    
    def display_all(self):
        return self.books
    
    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.issue():
            self.save()
            return True
        return False
    
    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book:
            book.return_book()
            self.save()
            return True
        return False
    
    def save(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass
    
    def load(self):
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
        except:
            self.books = []
