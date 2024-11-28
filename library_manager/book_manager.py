import json
import os
from typing import List, Dict, Optional

class Book:
    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class BookManager:
    def __init__(self, data_file: str = 'books.json'):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self) -> List[Dict]:
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, 'r') as file:
            return json.load(file)

    def save_books(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int):
        book_id = len(self.books) + 1
        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id: int):
        self.books = [book for book in self.books if book["id"] != book_id]
        self.save_books()

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> List[Dict]:
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book["title"].lower()]
        if author:
            results = [book for book in results if author.lower() in book["author"].lower()]
        if year:
            results = [book for book in results if book["year"] == year]
        return results

    def display_books(self):
        for book in self.books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

    def change_book_status(self, book_id: int, new_status: str):
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = new_status
                self.save_books()
                return
        raise ValueError("Book not found")
