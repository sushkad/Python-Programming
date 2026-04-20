arr = [1, 2, 2, 3, 4, 1, 5]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency:", frequency)