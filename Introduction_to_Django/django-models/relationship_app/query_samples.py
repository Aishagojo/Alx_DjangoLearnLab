from .models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()  # returns queryset of books
    except Author.DoesNotExist:
        return []


# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # returns queryset of books
    except Library.DoesNotExist:
        return []


# 3️⃣ Retrieve the librarian for a library
def get_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # returns Librarian instance
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage (you can run these in shell)
if __name__ == "__main__":
    print("Books by George Orwell:", books_by_author("George Orwell"))
    print("Books in Central Library:", books_in_library("Central Library"))
    print("Librarian of Central Library:", get_librarian("Central Library"))

