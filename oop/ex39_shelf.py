#!/usr/bin/env python3

"""A simple shelf calss containing all the books and prices."""


class Book():
    """A book containing the title, author and price."""

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Shelf():
    """A shelf containing the books and grand price."""

    def __init__(self):
        """Initialize with empty book list."""
        self.books = []

    def add_books(self, *books):
        """Add the books to list."""
        for book in books:
            self.books.append(book)

    def total_prices(self):
        """Return the grand total prices of the books on the shelf."""
        prices = 0
        for idx, book in enumerate(self.books):
            prices += book.price
        return prices

    def __repr__(self):
        """Rewrite the print."""
        return "\n".join("{0:5} | {1:6} | {2:3}".format(book.title, book.author, book.price) for book in shelf.books)

if __name__ == "__main__":
    shelf = Shelf()
    shelf.add_books(Book("ABC_1", "author 1", 10.99), Book("ABC_2", "author 2", 20.99))
    print("Total price:", round(shelf.total_prices(), 2))

    print(shelf)
