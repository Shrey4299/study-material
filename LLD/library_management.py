# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print(f"The book '{self.title}' is already checked out.")
        else:
            self.is_checked_out = True
            print(f"The book '{self.title}' has been checked out.")

    def return_book(self):
        if not self.is_checked_out:
            print(f"The book '{self.title}' was not checked out.")
        else:
            self.is_checked_out = False
            print(f"The book '{self.title}' has been returned.")

# Define the Patron class
class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.is_checked_out:
            print(f"Sorry, {self.name}. The book '{book.title}' is currently unavailable.")
        else:
            book.check_out()
            self.checked_out_books.append(book)
            print(f"{self.name} checked out the book '{book.title}'.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.return_book()
            self.checked_out_books.remove(book)
            print(f"{self.name} returned the book '{book.title}'.")
        else:
            print(f"{self.name} did not check out the book '{book.title}'.")

# Define the Library class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added the book '{book.title}' to the library.")

    def add_patron(self, patron):
        self.patrons.append(patron)
        print(f"Added patron '{patron.name}' to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"No book found with the title '{title}'.")
        return None

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        print(f"No patron found with the name '{name}'.")
        return None

# Usage example
library = Library()

# Add books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
library.add_book(book1)
library.add_book(book2)

# Add patrons to the library
patron1 = Patron("Alice")
patron2 = Patron("Bob")
library.add_patron(patron1)
library.add_patron(patron2)

# Patrons check out and return books
patron1.check_out_book(book1)
patron2.check_out_book(book1)  # Should be unavailable
patron1.return_book(book1)
patron2.check_out_book(book1)  # Should succeed
