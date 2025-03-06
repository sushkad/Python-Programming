from collections import Counter

str = "2790"

int_num =int(str)
print(int_num)
print(type(int_num))


string = "hello"
arr = ["apple", "apple", "orange"]


reversed_string = string[::-1]
print("Reversed string:", reversed_string)

frequency = Counter(arr)
duplicates = [item for item, count in frequency.items() if count>1 ]
print("qa", duplicates)