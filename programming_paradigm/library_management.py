class Book:
    """A class representing a single book in the library."""

    def __init__(self, title, author):
        """Initialize a book with its title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  

    def check_out(self):
        """Mark the book as checked out if it’s available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  

    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        Marks it as unavailable if found and available.
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"'{book.title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available or does not exist.")

    def return_book(self, title):
        """
        Return a book by title.
        Marks it as available if it was previously checked out.
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"Book '{title}' was not checked out or not found in the library.")

    def list_available_books(self):
        """Display all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
