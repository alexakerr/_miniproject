import re

from os import system
from author import Author
from user import User
from book import Book


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def add_author(self, author):
        self.authors.append(author)

    def display_all_books(self):
        for book in self.books:
            book.display_info()
            print()

    def display_all_users(self):
        for user in self.users:
            user.display_info()
            print()

    def display_all_authors(self):
        for author in self.authors:
            author.display_info()
            print()



#---------------------------------------------

# regex - 
def validate_menu_choice(input_str, menu_length):
    while True:
        choice = input(input_str)
        if re.match("^[1-{}]+$".format(menu_length), choice):
            return int(choice)
        else:
            print("Invalid input. Please enter a number between 1 and {}.".format(menu_length))


#---------------------------------------------

def main_menu(library):
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = validate_menu_choice("Enter your choice: ", 4)

        if choice == 1:
            book_menu(library)
        elif choice == 2:
            user_menu(library)
        elif choice == 3:
            author_menu(library)
        elif choice == 4:
            print("Exiting the program.")
            break


# book menu
def book_menu(library):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")

        choice = validate_menu_choice("Enter your choice: ", 6) #1

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            genre = input("Enter the genre of the book: ")
            publication_date = input("Enter the publication date of the book: ")
            new_book = Book(title, author, isbn, genre, publication_date)
            library.add_book(new_book)
            print("Book has been added successfully!")
       
        elif choice == 2: # Borrow a book
            title = input("Enter the title of the book you want to borrow: ")
            book = find_book(library, title)
            if book:
                if book.available:
                   user_id = input("Enter your user ID: ")
                   user = find_user(library, user_id)
                if user:
                 user.borrow_book(book)
            else:
                print("Sorry, this book is not available for borrowing.")
        elif choice == 3: # Return a book
            title = input("Enter the title of the book you want to return: ")
            book = find_book(library, title)
            if book:
                user_id = input("Enter your user ID: ")
                user = find_user(library, user_id)
            if user:
                user.return_book(book)

        elif choice == 4: # Search for a book
            title = input("Enter the title of the book you want to search for: ")
            book = find_book(library, title)
            if book:
                print("Book found:")
                book.display_info()
            else:
             print("Book not found.")

        elif choice == 5: # Display all books
            library.display_all_books()
        #break
        elif choice == 6:
            break



# user menu
def user_menu(library):
    while True:
        print("\nUser Operations:") #\n
        print("1. Add a new user")
        print("2. View the user details")
        print("3. Display all of the users")
        print("4. Back to main menu")

        choice = validate_menu_choice("Enter your choice: ", 4) #1-4 

        if choice == 1:
            name = input("Enter the name of the user: ")
            library_id = input("Enter the library ID of the user: ")
            new_user = User(name, library_id)
            library.add_user(new_user)
            print("User added successfully!")
        elif choice == 2: # view user details
            pass
        elif choice == 3:
            print("\nAll Users:")
            library.display_all_users()
        elif choice == 4:
            break

def author_menu(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all of the authors")
        print("4. Back to the main menu")

        choice = validate_menu_choice("Enter your choice: ", 4)

        if choice == 1:
            name = input("Enter the name of the author: ")
            biography = input("Enter the biography of the author: ")
            new_author = Author(name, biography)
            library.add_author(new_author)
            print("Author was added successfully!")
        elif choice == 2: # view authors details
            pass
        elif choice == 3:
            print("\nAll Authors:")
            library.display_all_authors()
        # break
        elif choice == 4:
            break


#finish
if __name__ == "__main__":
    library = Library()
    main_menu(library)





'''
Hello ! 
When you first open the app you will have the options to choose what class you would like to focus on. Your choices will be for book (choice 1), user (choice 2) or author (choice 3) operations or of course the option to quit (choice 4).
If you enter choice 1, you will then have the options to add (choice 1) a book by entering the title, author, isbn, genre and publication date.
If you enter choice 2, you will then have the choices to add a new user (choice 1), view the user details (choice 2), display all of the users (choice 3 ) or go back to the main menu.
Once back at the main menu if you select choice 3, you will be looking at author operations are to add a new author (choice 1), view the author details(choice 2), display all of the authors(choice 3)
'''
        