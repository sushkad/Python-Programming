

r = "Root"
rev = r[::-1]
print(rev)



s = "sush"
rev = ""

for char in s:
    rev = char + rev

print(rev)


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Max"))
print(is_palindrome("abdv"))



nums = [1,2,1,3,1,4,1,5]

dups = [x for x in set (nums) if nums.count(x) > 1]

print(dups)
