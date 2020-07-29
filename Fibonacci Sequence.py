num = input("How many Fibonacci Numbers do you want? Please enter: ")
num1 = int(num//2)

x = 0
y = 1

for i in range(num1):
    print(x)
    print(y)
    x = x + y
    y = y + x
