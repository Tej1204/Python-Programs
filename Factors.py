import math

num = input("Please enter a number: ")
num = int(num)
print("\nThese are the factors: ")

for i in range(num+1):
    if i == 0:
        continue
    div = num % i
    if div == 0:
        print(i)