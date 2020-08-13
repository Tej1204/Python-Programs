def reverse_list(mylist):
    mylist1 = []
    for i in range(1, num_of_items + 1):
        mylist1.append(mylist[-i])
    return mylist1


num_of_items = int(input("How many items in the list: "))
mylist = []

for i in range(num_of_items):
    ele = input("Enter an element: ")
    mylist.append(ele)

print("\nThe reversed list is: ")
print(reverse_list(mylist))