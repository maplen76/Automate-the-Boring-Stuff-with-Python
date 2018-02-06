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
    
# List to Dictionary Function for fantasy game inventory
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] = 1 + inventory.get(i,0)
        else:
            inventory.setdefault(i, 1)
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

    
