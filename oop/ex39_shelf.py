#!/usr/bin/env python3

"""A simple shelf calss containing all the books and prices."""


class Book():
    """A book containing the title, author and price."""

    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf():
    """A shelf containing the books and grand price."""

    # note 'width' here is a instance/object attribute not class attribute
    # compare this to ex40 for the class attribute
    def __init__(self, width=10):
        """Initialize with empty book list."""
        self.width = width
        self.current_width = 0
        self.books = []

    def add_books(self, *books):
        """Add the books to list."""

        '''
        for book in books:
            if self.current_width < self.width:
                self.books.append(book)
                self.current_width += book.width
            else:
                # print(f"sorry! excceeded max shelf width {self.width}")
                raise ValueError(f"sorry! excceeded max shelf width {self.width}")
        '''

        for book in books:

            ### check in in side of loop!!!
            if self.current_width + book.width > self.width:
                raise ValueError(f"sorry! excceeded max shelf width {self.width}")
            self.books.append(book)
            self.current_width += book.width

    def total_prices(self):
        """Return the grand total prices of the books on the shelf."""
        prices = 0
        for idx, book in enumerate(self.books):
            prices += book.price
        return prices

    def has_book(self, title):
        """Check if has the book with the given title."""
        if title in [book.title for book in self.books]:
            print("Book found")
            return True
        else:
            print("Book not found")
            return False

    def __repr__(self):
        """Rewrite the print."""
        return "\n".join("{0:5} | {1:6} | {2:3} | {3:1}".format(book.title, book.author, book.price, book.width) for book in shelf.books)


if __name__ == "__main__":
    shelf = Shelf(width=3)
    shelf.add_books(Book("ABC_1", "author 1", 10.99, 2), Book("ABC_2", "author 2", 20.99, 8))
    print("Total price:", round(shelf.total_prices(), 2))

    print(shelf)
    shelf.has_book("ABC_1")
    shelf.has_book("abcefg")

    # try to add another book which raising an exception due to excceed the width limit of the shelf
    shelf.add_books(Book("ABC_3", "author 3", 30.99, 5))
    print(shelf)
