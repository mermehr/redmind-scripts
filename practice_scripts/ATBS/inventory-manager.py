# Simple dictionary script for adding and merging lists

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print("Total number of items: ", item_total)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

while True:
    print('Type attack to slay the, or inv to display inventory or hit enter to quit. ')
    question = input('> ').split()

    if question[0] == 'attack':
        inv = add_to_inventory(inv, loot)
        print('You have defeated the dragon and gained:')
        print(loot)
    elif question[0] == 'inv':
        display_inventory(inv)