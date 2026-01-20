

# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# Constructor name should be _init_
# new keyword is not required when you create object


class Calculator:
    num = 100  # class variable
    # default constructor

    def __init__(self):
        print("Constructor")




    def getData(self):
        print("Execute method in class")

obj = Calculator()
obj.getData()
print(obj.num)