
# classes are user defined blueprint or prototype

#  + , *  , + , Constant

# Methods , class variables , instance variable and constructor
# object for your classes


class Calculator:
    num  = 100

    def getData(self):
        print("getting data")

obj = Calculator()   # syntax to create  object in python
obj.getData()

print(obj.num)