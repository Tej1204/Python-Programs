num = input("Enter a number: ")
num = int(num)
sum = 0

while True:
    dig = num % 10
    dig1 = dig * (10**(len(str(num))-1))
    sum = sum + dig1
    num = num//10
    if num == 0:
        break

print("\nThe number reversed is: ")
print(sum)