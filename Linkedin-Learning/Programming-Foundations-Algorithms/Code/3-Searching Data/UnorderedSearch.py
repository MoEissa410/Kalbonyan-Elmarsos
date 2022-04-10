# search for item in an unordered list
items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def find_item(item, itemList):
    for i in range(0, len(itemList)):
        if item == itemList[i]:
            return i

    return None


print(find_item(87, items))
print(find_item(250, items))
