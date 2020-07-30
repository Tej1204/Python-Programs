num = input("Enter any number: ")
num = int(num)
sum = 0

while num > 0:
    dig = num % 10
    sum = sum + dig
    num = num//10

print("\nThe sum of digits is: ")
print(sum)
