from collections import Counter

def find_frequency(arr):
    return Counter(arr)

str = "sushant kadam"
arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
print(find_frequency(arr))

print("reverse order",arr[::-1])
smallest_arr =min(arr)
print("small array",smallest_arr)


#List

values = [2,8,"python",6.0]

print(values[3])
print(values)


#Tuple

number = [1, 99, "sushant, 5.6"]

print(number[1])
print(number)

number [2] = "SUSHANT"


#Dictionary

dic = {"a" :2 ,4 : "cbd","c":"hello world"}

print(dic[4])
print(dic["c"])