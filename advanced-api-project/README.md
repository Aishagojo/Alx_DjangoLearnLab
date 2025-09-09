# Advanced API Project - Book Management

This project is built with Django REST Framework and demonstrates custom and generic views with permissions for CRUD operations.

## Endpoints

### Book List
- **URL:** `/api/books/`
- **Method:** GET
- **Description:** Retrieve a list of all books.
- **Permission:** Readable by anyone.

### Book Detail
- **URL:** `/api/books/<id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific book by its ID.
- **Permission:** Readable by anyone.

### Book Create
- **URL:** `/api/books/create/`
- **Method:** POST
- **Description:** Add a new book.
- **Permission:** Only authenticated users.

### Book Update
- **URL:** `/api/books/<id>/update/`
- **Method:** PUT
- **Description:** Update details of an existing book.
- **Permission:** Only authenticated users.

### Book Delete
- **URL:** `/api/books/<id>/delete/`
- **Method:** DELETE
- **Description:** Remove a book from the database.
- **Permission:** Only authenticated users.

## Authentication
- Use Django’s superuser or any authenticated user to test POST, PUT, DELETE.
- Read operations do not require authentication.

## Notes
- The Book model has a validation to prevent `publication_year` being in the future.
- Author and Book have a one-to-many relationship; each book belongs to one author.

