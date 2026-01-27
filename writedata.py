import reader

#file = open ('test.txt')
#file.readline()
#file.close()

# read the file and store all the lines in the list
# reverse the list
# write the list back to the file



with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)

    with open('test.txt', 'w') as f:
        for line in content:
            f.write(line)






