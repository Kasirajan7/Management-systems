import sys
class Library:
    def __init__(self,listOfBooks):
        self.availableBook=listOfBooks
    def displayavailableBooks(self):
        print()
        print("--------------Available Books-----------")
        for book in self.availableBook:
            print(book)
    def lendBooks(self,requestedBook):
        if requestedBook in self.availableBook:
            print("Requested book is borrowed")
            self.availableBook.remove(requestedBook)
        else:
            print("Sorry the book is not available")
    def addBooks(self,returnedBook):
        self.availableBook.append(returnedBook)
        print("You have returned the book successfully")
    
class Customer:
    def requestBook(self):
        print("---------------Enter the wook you want to borrow-------------")
        self.book=input()
        return self.book
    def returnBook(self):
        print("--------------------Enter the wook you want to return----------------")
        self.book=input()
        return self.book


library=Library(['Inspiring thoughts','Grow better and Rich','Lead World'])
customer=Customer()
while True:
    print("\n\n")
    print("Enter the option")
    print("1.Available Books")
    print("2.Request Book")
    print("3.Return Book")
    print("4.Quit")
    option=int(input())
    if option==1:
        library.displayavailableBooks()
    elif option ==2:
        requestedBook=customer.requestBook()
        library.lendBooks(requestedBook)
    elif option==3:
        returnedBook=customer.returnBook()
        library.addBooks(returnedBook)
    elif option==4:
        quit()
    else:
        print("Enter Valid option")


        
