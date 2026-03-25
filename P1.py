
'''
Q 1: Write a Python program to print "Hello, World!"

Q 2: Calculate the sum of two numbers entered by the user.

Q 3: Convert temperature from Celsius to Fahrenheit.
'''

def hello():

    print("Hello World")

hello()


num1 =  float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

result = num1 + num2
print(result)



celsius = float(input("Enter temperature in Celsius: :"))

fahrenheit = ((celsius * 9) / 5) + 32

print(fahrenheit)