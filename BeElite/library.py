class Book:
    def __init__(self, bookId, bookTitle, bookAuthor, publicationDate):
        self.bookId = bookId
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.publicationDate = publicationDate
        # track the borrowing state of the book
        self.isBorrowed = False
        self.borrowedBy = None
        self.dueDate = None

    # borrowing method
    def borrowBook(self, member, dueDate):
        if not self.isBorrowed:
            self.isBorrowed = True
            self.borrowedBy = member
            self.duedate = dueDate
            return True
        return False

    # Book return method
    def bookReturn(self):
        if self.isBorrowed:
            self.isBorrowed = False
            self.borrowedBy = None
            self.dueDate = None
            return True
        return False
 


# class for the library memeber
class LibraryMember:
    def __init__(self, memberId, name):
        self.memberId = memberId
        self.name = name

    def borrowBook(self, book, dueDate):
        return book.borrowBook(self, dueDate)

    def bookReturn(self, book):
        return book.bookReturn


# class for the librarian
class Librarian:
    def __init__(self, name):
        self.name = name

    def checkBookAvaiability(self, bookTitle):
        return not bookTitle.isBorrowed


# Creating Book instances
book1 = Book(bookId=1, bookTitle="The prag", bookAuthor="Dan Brown", publicationDate=2011)
book2 = Book(2, 'Age of Ultron', "Sam Klef", 2012)

# # Creating LibraryMember instances
libraryMember1 = LibraryMember(1, "James Bond")

# # Creating Librarian instance
libraryStaff = Librarian(name="Yon Yu")

# # borrowing books
# due_date = "2023-08-15"
# if libraryMember1.borrowBook(book1, due_date):
#     print(f"{book1.bookTitle} has been borrowed by {libraryMember1.name} until {due_date}")
# else:
#     print(f"{book1.bookTitle} is already borrowed or unavailable")


# # Checking due dates
if book2.isBorrowed:
    print(f"{book1.bookTitle} is borrowed by {book1.borrowedBy}")
    print(f"Due to be returned by: {book1.dueDate}")
else:
    print(f"{book1.bookTitle} is available")


# # Returning books
# if libraryMember1.bookReturn(book1):
#     print(f"{book1.bookTitle} has been returned by {libraryMember1.name}")
# else:
#     print(f"{book1.bookTitle} was not borrowed by {libraryMember1.name}")
