from collections import Counter
# Sample array and string
arr = [1, 2, 3, 4, 2, 5, 1, 6, 7, 8, 8]
string = "  Hello  World!  "

#frequency
freq = Counter(arr)
print(freq)

# larger element
larg_element = max(arr)
print(larg_element)

# small element
small_element = min(arr)
print(small_element)

#reverse order
print(arr[::-1])

# Duplicate
duplicate = [item for item, count in freq.items() if count > 1]
print(duplicate)

