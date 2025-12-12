"""
Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].


update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) should return [[3, "apples"], [8, "bananas"]].
update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].

"""

def update_inventory(inventory, shipment):
# arr inv
# arr received
# arr[1] = [1, "name"]
    dict_inv = {}
    for val in inventory:
        item=val[1]
        qty=val[0]
        dict_inv[item] = qty
    for val in shipment:
        item=val[1]
        qty=val[0]
        # if item in dict_inv.keys()
        if item in dict_inv.keys():
            dict_inv[val[1]] += val[0]
        else:
            dict_inv[val[1]] = val[0]
    arr = []
    for i in list(dict_inv.items()):
        arr.append([i[1],i[0]])
    return arr




if __ name __ == '__ main __':

    arr = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])
    print(arr)
    arr = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) 
    print(arr)

    arr= update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) 
    print(arr)

    arr = update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) 
    print(arr)