class Book:
    def __init__(self,title,author,year=None,genre=None):
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre
    def display_info(self):
        print(f"'{self.title}' is written by {self.author} in {self.year}.\n"
                  f"The genre of the book is {self.genre.lower()}.")
    def rate_book(self,rating=None):
        self.rating = rating
        if rating is not None and 0 <= rating <= 5:
            print(f"Your final rating is {self.rating}.")
        else:
            print("Error")
        
