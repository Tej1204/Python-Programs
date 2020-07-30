# num = input("Enter any number: ")
# power = len(num)
# num1 = int(num)
# sum = 0
#
#
# while num1 > 0:
#     dig = num1 % 10
#     dig1 = dig ** power
#     sum = sum + dig1
#     num1 = num1 // 10
#
# if sum == num:
#     print("\nThe number is Armstrong: ")
#     print("Both the sum and number are: ")
#     print(sum)
# else:
#     print("\nThe number is not Armstrong.")
#     print("Because the sum is: ")
#     print(sum)
def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count

def is_armstrong_number(num):
    #write function implementation
    power = count_digits(num)
    num1 = num
    sum = 0

    while num1 > 0:
        dig = num1 % 10
        dig1 = dig ** power
        sum = sum + dig1
        num1 = num1 // 10

    if sum == num:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('Enter a number:'))
    if is_armstrong_number(num):
        print("Given number is an armstrong number")
    else:
        print("Given number is not an armstrong number")