class Library:
    def __init__(self,books):
        self.books=books
        self.dict={}
    def showBooks(self):
        print("Books we have in Library:")
        for item,index in enumerate(self.books):
            print("\t",item,index)
    def lendBook(self,book):
        if book not in self.dict.keys():
            self.dict.update({book:book})
        #if book in self.books:
            print(f"You have been issued with: {book}")
            #self.books.remove(book)
            return True
        else:
            print(f"Sorry! {book} has been taken.")
            return False
    def addBook(self,book):
        self.books.append(book)
        print("Book has been added in list!")
    def returnBook(self,book):
        self.dict.pop(book)
        print(f"{book} Book has been returned in list!")

class Student:
    def reqBook(self):
        self.book=input("Enter the book you want to read: ")
        return self.book
    def addBook(self):
        self.book=input("Enter book you want to add: ")
        return self.book
    def returnBook(self):
        self.book=input("Enter book you want to return: ")
        return self.book
if __name__ == '__main__':
    library=Library(["R","Python","Java","JavaScript","C","CSS","HTML"])
    student=Student()
    while(True):
        msg="""**** You are in the Library ****
    1.Lists of books
    2.Request Book
    3.Add book
    4.Return book
    5.Exit from library"""
        print(msg)
        a=input("Enter your choice:\n")
        if a not in ["1","2","3","4","5"]:
            continue
        else:
            a=int(a)
        if a==1:
            library.showBooks()
        elif a==2:
            library.lendBook(student.reqBook())
        elif a==3:
            library.addBook(student.addBook())
        elif a==4:
            library.returnBook(student.returnBook())
        elif a==5:
            print("Thanks for using Library!")
            exit()
        else:
            print("please enter valid data!")