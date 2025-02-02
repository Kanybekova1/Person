from book import Book

# Ask the user how many books they want to create
n = int(input("How many books do you want to create? "))
books = []

# Creating N Book objects using the parameterized constructor
for i in range(n):
    print(f"\nEnter details for Book {i+1}:")
        
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    genre = input("Enter genre: ")

    # Create the book object
    book = Book(title, author, year, genre)
        
    # Save the book in the list
    books.append(book)

# Display book details
print("\n Book Information")
for book in books:
    book.display_info()

# Allow users to rate the books
for book in books:
    print(f"\nRate the book '{book.title}': ")
    rating = float(input("Enter your rating (0-5): "))
    book.rate_book(rating)


