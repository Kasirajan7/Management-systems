from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def signup():
        return 0
    def addMoney():
        return 0
    def displayDetails():
        return 0
    def login():
        return 0
    def validate():
        return 0
    def bookTicket():
        return 0
    def displaySeat():
        return 0
    
        

    
class Customer:
    def __init__(self):
        self.customerDb={}
        self.chnToban=[]
        self.finalend=[0,0]
        self.count=0


    def signup(self,name,password,amount):
        #[key][0]=name [key][2]=password [key][1]=amount
        self.loginId=randint(10000,99999)
        self.customerDb[self.loginId]=[name,password,amount]
        print("Your account has been created succesfully and your login ID is",self.loginId)
        
    def addMoney(self):
        print("Enter the amount to be added")
        amountToadd=int(input())
        self.customerDb[self.loginId][1]+=amountToadd
        self.displayDetails()
    def displayDetails(self):
        print("Login ID",self.loginId)
        print("Name:",self.customerDb[self.loginId][0])
        print("Amount:",self.customerDb[self.loginId][1],"\n\n")    
        
    def login(self):
        self.loginId=int(input("Enter the login id\n"))
        self.password=input("Enter the password\n")
        authenticate=self.validate(self.loginId,self.password)
        return authenticate

    def validate(self,loginId,password):
        if loginId in self.customerDb.keys():
            if password == self.customerDb[loginId][2]:
                print("Authentication is valid")
                self.loginId==loginId
                return True
            else:
                print("Authentication is invalid")
                return False
        else:
            return False

    def bookTicket(self,ticket):
        totalCost=50*ticket
        self.count+=ticket
        if self.count<30:    
            if self.customerDb[self.loginId][1]>totalCost:
                self.customerDb[self.loginId][1]-=totalCost
                
                for i in range(0,ticket):
                    self.chnToban.append(self.loginId)
            else:
                print("Insufficient Balance")
        else:
            self.count-=ticket
            print("No. of seats you entered is not available")
            print("No of Available seats:",30-self.count)
        self.displaySeat()
        
    def displaySeat(self):
        print(self.chnToban)


customer=Customer()
print("------------Welcome to SETC bus Ticket booking------------------")
print ("Enter the option")
while True:
    print("\n\n1.Login")
    print("2.Sign up")
    print("3.Exit\n")
    userChoice=int(input())
    if userChoice==1:
        authenticate=customer.login()
        print(authenticate)
        if authenticate is True:
            while True:
                print("\n\n1.Book tickets")
                print("2.Add Money to wallet")
                print("3.To display details")
                print("4.Go back to menu\n")
                userChoice1=int(input())
                if userChoice1==1:
                    print("Enter the number of tickects from chennai to bangalore")
                    tickets=int(input())
                    customer.bookTicket(tickets)
                elif userChoice1==2:
                    customer.addMoney()
                elif userChoice1==3:
                    customer.displayDetails()
                elif userChoice1==4:
                    break
        else:
            print("Authentication is failed")
    elif userChoice==2:
        print("Enter your name")
        name=input()
        print("Enter the amount")
        amount=int(input())        
        print("Enter the password")
        password=input()
        customer.signup(name,amount,password)

    elif userChoice==3:
        quit()
    elif userChoice==4:
        print("Enter valid option\n")
