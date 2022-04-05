stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for key in stuff:
        total += stuff[key]
        print(str(stuff[key]) + " " + key)
    print("Total number of items: " + str(total))

##displayInventory(stuff)