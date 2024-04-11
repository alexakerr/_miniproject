class Book:
    def __init__(self, title, author, ISBN, genre, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.publication_date = publication_date
        self.available = True

# show the info
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
        print(f"Publication Date: {self.publication_date}")
        print(f"Available: {'Yes' if self.available else 'No'}")



        