
# classes are user defined prototye

class One:              # create class
    num= 100

    def __init__(self, a, b):
        self.fnum = a
        self.snum = b
        print("Called auto when object is already created")
    def getData(self):
        print("execute method in class")

    def add(self):
        return self.fnum + self.snum

object = One(5,5)          # object
object.getData()
print(object.add())


# class variable
# instance variable