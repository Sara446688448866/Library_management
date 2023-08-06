class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author, genre):
        new_book = Book(book_id, title, author, genre)
        self.books.append(new_book)
        print(f"Book '{title}' has been added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                return
        print(f"Book with ID {book_id} not found in the library.")

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book found: {book.title} by {book.author} ({book.genre})")
                return
        print(f"Book with title '{title}' not found in the library.")

    def search_book_by_author(self, author):
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"Book found: {book.title} by {book.author} ({book.genre})")
                return
        print(f"Book by author '{author}' not found in the library.")

    def list_all_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
            return
        print("Books available in the library:")
        for book in self.books:
            print(f"{book.book_id}: {book.title} by {book.author} ({book.genre})")

if __name__ == "__main__":
    library = Library()
    
    while True:
        print("\n*** Alexandria Library Management System ***")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. List All Books")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            genre = input("Enter Book Genre: ")
            library.add_book(book_id, title, author, genre)
        
        elif choice == "2":
            book_id = int(input("Enter Book ID to remove: "))
            library.remove_book(book_id)
        
        elif choice == "3":
            title = input("Enter Book Title to search: ")
            library.search_book_by_title(title)
        
        elif choice == "4":
            author = input("Enter Book Author to search: ")
            library.search_book_by_author(author)
        
        elif choice == "5":
            library.list_all_books()
        
        elif choice == "0":
            print("Exiting Alexandria Library Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")
