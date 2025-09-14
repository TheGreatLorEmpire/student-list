class Book:
    def _init_(self, title, author, year, stock):
        self.title = title
        self.author = author
        self.year = year
        self.stock = stock

    def _str_(self):
        return f"{self.title} by {self.author} ({self.year}) - Stock: {self.stock}"


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books available.")
        for b in self.books:
            print(b)

    def search(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def remove(self, title):
        try:
            book = self.search(title)
            if book:
                self.books.remove(book)
                print(f"{title} removed.")
            else:
                raise ValueError("Book not found.")
        except ValueError as e:
            print(e)

library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        stock = int(input("Stock: "))
        library.add_book(Book(title, author, year, stock))
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        title = input("Enter book title to search: ")
        book = library.search(title)
        print(book if book else "Book not found.")
    elif choice == "4":
        title = input("Enter book title to remove: ")
        library.remove(title)
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice")