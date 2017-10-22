from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    def authenticate():
        return 0
    def withdraw():
        return 0
    def deposit():
        return 0
    def displayBalance():
        return 0

class SavingsAccount:
    def __init__(self):
        #[key][0]=>name ; [key][1]=>balance
        self.savingAccounts={}
    def createAccount(self,name,initialDeposit):
        self.accountNumber=randint(10000,99999)
        self.savingAccounts[self.accountNumber]=[name,initialDeposit]
        print("Your account has been created successfully.Your account number:",self.accountNumber)
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0]==name:
                print("Authentication is successful")
                self.accountNumber==accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False
        
    def withdraw(self,withdrawalAmount):
        if withdrawalAmount >self.savingAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingAccounts[self.accountNumber][1]-=withdrawalAmount
            print("Your amount has been withdrawaled successfully")
            self.displayBalance()
    def deposit(self,depositAmount):
        self.savingAccounts[self.accountNumber][1]+=depositAmount
        self.displayBalance()

    def displayBalance(self):
        print("Available Balance:",self.savingAccounts[self.accountNumber][1])

savingsAccount=SavingsAccount()
while True:
    print("1.Create a new Account")
    print("2.Access an existing account")
    print("3.Exit")
    userChoice =int(input())
    if userChoice is 1:
        print("Enter your name")
        name=input()
        print("Enter the initial deposit")
        initialDeposit=int(input())
        savingsAccount.createAccount(name,initialDeposit)
    elif userChoice is 2:
        print("Enter your name")
        name=input()
        print("Enter the account number")
        accountNumber=int(input())        
        authenticationStatus=savingsAccount.authenticate(name,accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to menu")
                userChoice=int(input())
                if userChoice is 1:
                    print("Enter withdraw amount")
                    withdrawAmount=int(input())
                    savingsAccount.withdraw(withdrawAmount)
                elif userChoice is 2:
                    print ("Enter the amount to deposit")
                    depositAmount=int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
            quit()










                
