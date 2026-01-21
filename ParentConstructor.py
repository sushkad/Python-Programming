

# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# Constructor name should be _init_
# new keyword is not required when you create object


class Calculator:
    num = 100  # class variable
    # default constructor

    def __init__(self , a, b):
        self.first = a
        self.second = b

        print("Constructor")


    def getData(self):
        print("Execute method in class")

    def summation(self):
         return self.first + self.second + Calculator.num

obj = Calculator(2,3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.summation())