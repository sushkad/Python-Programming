
'''
person = {"Rahul", 25, 5.9}


print("Age:", person[1])

try:
    person[0] = "Sushant"
except TypeError as e:
    print("Error:", e)

 '''

person = ("Rahul", 25, 5.9)

temp = list(person)
temp[0] = "Amit"

person = tuple(temp)

print(person)