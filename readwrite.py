

file = open('test.txt')

#print(file.readline())
#print(file.read(4))     eiter use read() or readline()

#print(file.close())

# print line by line using readline method

#line = file.readline()

#while line!="":
#    print(line)
#    line = file.readline()



# One more method

#values = [abc,"abcd",sushant]

for line in file.readlines():
    print(line)
file.readline()

file.close()