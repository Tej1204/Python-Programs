num_of_items = int(input("How many items in the list: "))
mylist = []

for i in range(num_of_items):
    ele = input("Enter an element: ")
    mylist.append(ele)

deli = input("Enter a valid delimiter: ")

print(deli.join(mylist))