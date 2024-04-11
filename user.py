class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.library_id}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(book.title)