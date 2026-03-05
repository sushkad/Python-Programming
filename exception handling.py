
ItemsInCart = 0

def add_to_cart(items_to_add):

    global ItemsInCart

    if items_to_add < 0:
        raise Exception("You can't add negative numbers")

    if ItemsInCart +  items_to_add > 5:
        raise Exception("You can't add more than 5 items")

    ItemsInCart += items_to_add
    print(f"{items_to_add} added to cart. Total in cart is {ItemsInCart}")


try:
    add_to_cart(2)
    add_to_cart(-1)

except Exception as e:
    print(e)
