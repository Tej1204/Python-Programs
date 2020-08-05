def convert_binary(number):
    binary_code = 0
    while number > 0:
        for i in range(number):
            dig = number % 2
            dig = dig * 10 ** (i)
            number = number // 2
            binary_code = binary_code + dig
    print(binary_code)


number = int(input("Please enter a number: "))
print('\nThe Binary code for ' + str(number) + ' is: ')
convert_binary(number)