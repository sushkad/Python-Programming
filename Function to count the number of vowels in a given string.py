


def count_vowels(s):

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = sum(1 for char in s if char in vowels)

    return count


string = input("Enter a string: ")
print(f"The number of vowels in {string} is {count_vowels(string)}")
