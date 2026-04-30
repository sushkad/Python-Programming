

def reverse_str(s):
    return s[::-1]

print(reverse_str("aeious"))


def palindrome(s):
    return s ==s[::-1]

print(palindrome("a"))


def vowels(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in s:
