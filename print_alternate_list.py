num_of_ele = int(input('How many items in the list: '))
list_of_items = []

for i in range(num_of_ele):
    ele = input("Enter an item for the list: ")
    list_of_items.append(ele)

print(list_of_items[1::2])