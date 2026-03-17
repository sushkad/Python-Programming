
num = 8

is_prime = True

if num <=1:
    is_prime = False

else:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break


print("prime" if is_prime else "not prime")