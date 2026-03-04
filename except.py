try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")