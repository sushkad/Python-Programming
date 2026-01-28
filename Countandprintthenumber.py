'''
Count Lines in a File
Objective: Count and print the number of lines in a file.

Instructions:

Use the attached text file "file1.txt"

Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.

Expected result:

Total number of lines: 5

'''




with open("test.txt", "r") as file:
    line_count = 0

    for line in file:
        line_count += 1

print(f"Total number of lines: {line_count}")