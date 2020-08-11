num_of_ele = int(input('How many items in the list: '))
list_of_items = []

for i in range(num_of_ele):
    ele = input("Enter an item for the list: ")
    list_of_items.append(ele)

for i in range(1,num_of_ele,2):
    print(list_of_items[i])

# print(list_of_items[1::2])