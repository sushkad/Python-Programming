from ParentConstructor import Calculator


# Inheritance - acquire properties of parent class


class childimpl(Calculator):

    num2 = 200
    def __init__(self):
        Calculator.__init__(self,2,4 )   #

    def getCompledata(self):
        return self.num2 + self.num + self.summation()


obj = childimpl()
print(obj.getCompledata())





