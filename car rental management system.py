class Cars:
    def hatchback(self,day):
        self.day=day
        self.total=30*self.day
        print("The total fare for {} days is ${}\n\n".format(self.day,self.total))

    def sedan(self,day):
        self.day=day
        self.total=50*self.day
        print("The total fare for {} days is ${}\n\n".format(self.day,self.total))
        
    def suv(self,day):
        self.day=day
        self.total=100*self.day
        print("The total fare for {} days is ${}\n\n".format(self.day,self.total))

class Days:
    def totalDays(self):
        print("Enter numbr of days you wat to borrow a car")
        self.days=int(input())
        return self.days
cars=Cars()
days=Days()
while True:
    print("------------------Types of car------------")
    print("1.Hatchbck -$30")
    print("2.Sedan    -$50")
    print("3.SUV      -$100")
    print("4.Quit")
    print("\n")
    print("Enter your choice\n")
    userChoice=int(input())
    if userChoice==1:
        day=days.totalDays()
        cars.hatchback(day)
    elif userChoice==2:
        day=days.totalDays()
        cars.sedan(day)
    elif userChoice==3:
        day=days.totalDays()
        cars.suv(day)
    elif userChoice==4:
        quit()
    else:
        print("Enter valid Choice")
        
