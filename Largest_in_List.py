def find_maximum(mylist):
    maximum = float("-inf")
    for i in range(1,len(mylist)):
        if mylist[i] > maximum:
            maximum = mylist[i]
    return maximum


mylist = []
amount = input("How many numbers in a list: ")
a = int(amount)

for i in range(a):
    num = int(input("Enter number: "))
    mylist.append(num)

max_result = find_maximum(mylist)

print("\nLargest number in the list is: ")
print(max_result)
# print(max(mylist))