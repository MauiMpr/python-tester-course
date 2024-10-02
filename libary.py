class Book:
    def __init__ (self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def search_title(self, title):
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.book))
    
    def search_author(self, author):
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.book))
    
    def search_available(self, title, available):
        search_available = lambda book: setattr (book, 'available', available) if book.title.lower() == title.lower() else None
        list(map(search_available, self.book))
    

book1 = Book("12 Rules For Life", "Jordan Peterson", "Available")
book2 = Book("Being You", "Anil Seth", "Available")
book3 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", "Available")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Search by book title :  12 Rules For Life")
for book in library.search_title("12 Rules For Life"):
    print(f"{book.title} by {book.author}")

print("Search by author : Anil Seth")
for book in library.search_author("Anil Seth"):
    print(f"author {book.author} {book.title}")

print("\nAvailability of 'The Brothers Karamazov :")
for book in library.search_title("The Brothers Karamazov"):
    print(f"- {book.title} is {'available' if book.available else 'not available'}")

    















