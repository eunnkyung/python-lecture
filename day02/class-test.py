class Greeting() :  
    def hello(self) :
        print("hello")

    def hi(self) :
        print("hi")

you = Greeting()
you.hello()
you.hi()


jung = Greeting()
jung.hello()
jung.hi()

class Student() :
    def __init__(self,name,age, hobby):
        self.name =  name
        self.age =  age
        self.hobby =  hobby
    def printInfo(self) : 
        print(f"name : {self.name}, age : {self.age}, hobby : {self.hobby}")

you = Student("유재석",50,"커피")
you.printInfo()


#class Mother() :
#    def character(self) :
#        print("예쁘다")
#        print("똑똑하다")

#class Daughter(Mother) : 
#    def character(self) :
#        super().character() 
#        print("운동도 잘한다")
#mother = Mother()        
#daughter = Daughter()        
#mother.character()
#print("===========================")
#daughter.character()


class Mother() :
    def __init__(self):
        print("예쁘다")
        print("똑똑하다")

    @staticmethod
    def greeting(msg) :
        print(msg)


class Daughter(Mother) :
    def __init__(self):
        super().__init__()
        print("운동도 잘한다")

print("===========================")
mother = Mother()        
daughter = Daughter()        
print("===========================")
Mother.greeting("hello static")


class BankAccount :
    def __init__(self,name,money = 0):
        self.name = name
        self.money = money

    def deposit(self,amount):
        self.money+=amount
        print(f"{amount} 입금 / 잔액 : {self.money}")

    def withdraw(self,amount):
        if self.money >= amount :
            self.money-=amount
            print(f"{amount} 출금 / 잔액 : {self.money}")
        else :
            print("잔고 부족")

#아래 정보를 참고해서 class 만들어 보기
acc = BankAccount("김철수", 10000)
acc.deposit(5000)   # 5000원 입금
acc.withdraw(3000)  # 3000원 출금
acc.withdraw(15000) # 잔액 부족

