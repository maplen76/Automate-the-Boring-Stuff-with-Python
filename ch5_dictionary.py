# Practice Projects
# Fantasy Game Inventory
inventory = {'rope': 1, 
             'torch': 6, 
             'gold coin': 42, 
             'dagger': 1, 
             'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    totalItem = 0
    for k, v in inventory.items():
        numberItem = inventory.get(k, 0)
        print(str(numberItem) + '    ' + k)
        totalItem = totalItem + numberItem
    print('Total number of items: ' + str(totalItem))
