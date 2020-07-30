import math

num = input("Please enter a number here: ")
num = int(num)
if 1 < num <= 3:
    print("This number is inherently prime.")
    exit()
n = int(math.sqrt(num)//1)
is_prime = True

for i in range(2,n+1):
    if num % i == 0:
        is_prime = False
        print("Number is not prime.")
        break

if is_prime:
    print("Number is prime.")