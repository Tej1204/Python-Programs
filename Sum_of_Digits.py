num = input("Enter any number: ")
num = int(num)
sum = 0

while True:
    dig = num % 10
    sum = sum + dig
    num = num//10
    if num == 0:
        break

print("\nThe sum of digits is: ")
print(sum)
