class Library:
    def __init__(self,books,name):
        self.books=books
        self.name=name
        self.dict={}
    def showBooks(self):
        print("List of books in library")
        for item,index in enumerate(self.books):
            print(" ",item,index)
    def reqBook(self,book,name):
        if book not in self.dict.keys():
            self.dict.update({book:name})
            print(f" {book} is in the list and is issued to {name}")
            return True
        else:
            print(f"Sorry, Book has been taken by {self.dict[book]}")
            return False
    def addBook(self,book):
        self.books.append(book)
        print("Book has been added to the list")
    def returnBook(self,book):
        self.dict.pop(book)
        print(f"{book} has been returned!")



if __name__ == '__main__':
    lib=Library(["R","CSS","JS","Python","Swift","ML","Ruby","HTML"],"codeWithMe")
    while(True):
        msg="""
        ******Your in Library******
        1.List of books
        2.Request book
        3.Add book
        4.Return book
        5.Exit from library"""
        print(msg)
        a=input("Enter your choice: ")
        if a not in ["1","2","3","4","5"]:
            continue
        else:
            a=int(a)
        if a==1:
            lib.showBooks()
        elif a==2:
            book=input("Enter the book you want to read: ")
            name=input("Enter your name: ")
            lib.reqBook(book,name)
        elif a==3:
            book=input("Enter the book you want to add: ")
            lib.addBook(book)
        elif a==4:
            book=input("Enter the book you want to return: ")
            lib.returnBook(book)
        elif a==5:
            print("Thanks for using library")
            exit()
        else:
            print("Enter valid data!")