# Function to count vowels in a string


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Input string
string = input("Enter a string: ")

# Print the count of vowels
print(f"The number of vowels in the string is: {count_vowels(string)}")