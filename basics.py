
# Expected Output = [1, 3, 5]
# Explanation:
# – List comprehension filters elements where remainder when divided by 2 is not zero
# – Keeps only odd numbers
numbers =[1,2,3,4,5,6]
#odd_numbers = [x for x in numbers if x % 2 !=0]
#print(odd_numbers)


# Explanation:
# – The for loop iterates through each number
# – % 2 == 0 checks for even numbers
# – Uses f-string for formatted output
# Expected Output = 1 is odd 2 is even 3 is Odd
for num in numbers:
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# reverse the string

text = "data Science"

reversed_text = text[::-1]
print(reversed_text)


# Filter names that start with the letter "A" (case-sensitive).
# Explanation:
# – startswith("A") checks if a string starts with 'A'
# – List comprehension filters matching names

names = ["Sushant", "Rahul" , "Sagar", "Sayan"]

a_names = [name for  name in names if name.startswith("S")]
print(a_names)


# Create a new list containing only numbers divisible by 5 and greater than 20.

# Expected Output: [25, 30, 45, 60]

numbers = [10,25,30,45,60]

filtered = [x for x in numbers if x % 5 ==0 and x > 20]
print(filtered)

# Explanation:
# – Filters values divisible by 5 using x % 5 == 0
# – Also checks x > 20 to apply both conditions


'''
You have a sentence:    
text = "Python is simple but powerful"

Question:  
Count the number of words in the sentence.

Expected Output:  
5

'''
text = "Python is simple but powerful"
words = text.split()
print(len(words))

# Explanation:
# – split() breaks the sentence into words
# – len()counts the number of words in the list

#You have a list of numbers:
numbers = [3, 5, 7, 2, 8]

#Question:
#Find the maximum number in the list without using max()
#Expected Output:  8

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)

# Explanation:
# – Start by assuming the first number is the largest
# – Loop through and update max_num if a bigger value is found


z = 5
y = 2
print(type(z))   # return data type
print(id(z))     # return memory address

print(z + y)

int("10")
print(int)

# sort the list in ascending order and remove duplicates
numbers = [5,2,9,1,5,6,8,10,11,12,1,2]

unique_sorted = sorted(set(numbers))
print(unique_sorted)

# Explanation:
# – set() removes duplicates
# – sorted() arranges the list in order



























