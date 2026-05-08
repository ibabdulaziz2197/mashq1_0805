# 2
class Atributlar:
    class Student:
        def __init__(self, name, age, grade, password):
            self.name = name
            self.age = age
            self._grade = grade
            self.__password = password

        def study(self, hours):
            self._grade += hours

        def check_password(self, pw):
            return self.__password == pw

        def info(self):
            print(f"{self.name} Grade:{self._grade}")


    ali = Student("Ali", 20, 70, "1234")


    ali.study(10)
    ali.info()
    print(ali.check_password("1234"))
    print(ali.check_password("0000"))

# 3
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if pin != self.__pin:
            print("Wrong pin")
        else:
            self._balance -= x

    def check_balance(self):
        print(self._balance)



acc = BankAccount("Ali", 100, "1111")

acc.deposit(50)
acc.check_balance()

acc.withdraw("0000", 50)

acc.withdraw("1111", 50)
acc.check_balance()

# 4
class Phone:
    def __init__(self, model, battery, imei):
        self.model = model
        self._battery = battery
        self.__imei = imei

    def call(self, minutes):
        self._battery -= minutes
        if self._battery < 0:
            self._battery = 0

    def charge(self, x):
        self._battery += x
        if self._battery > 100:
            self._battery = 100

    def info(self):
        print(f"Battery:{self._battery}")



phone = Phone("iPhone", 100, "123456789")

phone.call(20)
phone.info()

phone.charge(30)
phone.info()
