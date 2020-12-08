def addToInventory(inventory, addedItems):

    for i in addedItems:

        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1

    return inventory


def displayInventory(inventory):

    print("Inventory: ")
    items = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        items += v

    print("Total number of items: {}".format(items))


if __name__ == '__main__':
    inv = {"gold coin": 42, "rope": 1}
    dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
