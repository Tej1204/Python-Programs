num = int(input("Please enter a number: "))
print("\nThese are the factors: ")

for i in range(1,int(num ** 0.5)+1):
    if num % i == 0:
        print(i)
        print(num//i)