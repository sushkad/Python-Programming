from writedata import reader

ItemsInCart = 0

if ItemsInCart != 2:
   # raise Exception("The product count does not match")
    pass


assert(ItemsInCart == 0)


# try , Catch

try:
    with open('example.txt') as f:
        reader.read()

except Exception as e:
    print(e)

finally:
    with open('example.txt') as f:
        print("Cleaning up resources")