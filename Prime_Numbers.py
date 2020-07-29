import math

num = input("Please enter a number here: ")
num = int(num)
if num == 0 or num == 1 or num == 2 or num == 3:
    print("This number is inherently prime.")
    exit()
n = int(math.sqrt(num)//1)

for i in range(n+1):
    if i == 0 or i == 1:
        continue
    div = num % i
    if div == 0:
        print(i)
        print("Number is not prime")
        break

if div != 0:
    print("Number is prime.")