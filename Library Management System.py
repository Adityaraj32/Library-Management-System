class Library:
    def __init__(self,library_name,list_books):
        self.library = library_name
        self.books = list_books
    def displayAvailableBook(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(f" *  {book}")
    def lendBook(self,borrower_name,borrow_book_name):
        if borrow_book_name.lower() in self.books.lower():
            print(f"Mr {borrower_name}, {borrow_book_name} books is given to you keep it safe and kindley return it in 30 days")
            self.books.remove(borrow_book_name)
        else:
            print("The Book is already issued to someone else .Wait until the book is returned")
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thank you for returning this book")
    def addBook(self,adderName,addedBookName):
        if addedBookName not in self.books:
            self.books.append(addedBookName)
        else:
            print("The Book is already present")

Harrylibrary = Library("Harry_library", ["The Breif History of time","Hyperlink","Bhasa ratna","English Grammer"])

while True:
    Library_welcome = '''\n Welcome to Libray Management System 
    Please Choose an option:
    1.Listing all book
    2.Request a book
    3.Return a book
    4.Add a book
    5.Exit Library\n
    '''
    print(Library_welcome)
    User_choose = int(input("Please Enter: "))
    if User_choose == 1:
        Harrylibrary.displayAvailableBook()
    if User_choose == 5:
        print("Thanks for comming")
        break
    if User_choose == 2:
        nameOfTake = input("Enter your name: ")
        nameOfBookTake = input("Enter the name of book: ")
        Harrylibrary.lendBook(nameOfTake, nameOfBookTake)
    if User_choose == 3:
        returnBookName = input("Enter the name of book: ")
        Harrylibrary.returnBook(bookName)
    if User_choose == 4:
        print("\nThanks! for adding book\n")
        userAdderName = input("Enter your name: ")
        userAddBook = input("Enter the name of book: ")
        Harrylibrary.addBook(userAdderName, userAddBook)

        

