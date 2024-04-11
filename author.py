class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Biography: {self.biography}")