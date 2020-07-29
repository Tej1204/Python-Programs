list = []

amount = input("How many numbers in a list: ")
a = int(amount)

for i in range(a):
    num = int(input("Enter number: "))
    list.append(num)

list.sort()

print("\nLargest number in the list is: ")
print(list[-1])
print(list)
