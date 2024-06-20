class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookFormatter:
    @staticmethod
    def format(book):
        return f"{book.title} by {book.author}"

book = Book("The Hobbit", "J.R.R. Tolkien")
formatted_book = BookFormatter.format(book)
print(formatted_book)
