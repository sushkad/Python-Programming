
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times
i = 1

while i > 1:
    if i == 9:
        i = i-1
        continue
    if i == 3:
        break
    print(i)

    i = i -1
print("While lop execute here")

'''
i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
'''


