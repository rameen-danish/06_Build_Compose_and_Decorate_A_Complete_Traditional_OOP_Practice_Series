class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage:
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1998", "Jannat k Patte")

print("Total books:", Book.total_books)
