num = input("Enter any number: ")
num1 = int(num)
num2 = num1
sum = 0

while True:
    dig = num2 % 10
    dig1 = dig ** len(str(num))
    sum = sum + dig1
    num2 = num2 // 10
    if num2 == 0:
        break

if sum == num1:
    print("\nThe number is Armstrong: ")
    print("Both the sum and number are: ")
    print(sum)
else:
    print("\nThe number is not Armstrong.")
    print("Because the sum is: ")
    print(sum)
