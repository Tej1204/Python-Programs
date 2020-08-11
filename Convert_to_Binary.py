def convert_binary(number):
    binary_code = []
    while number > 0:
        dig = number % 2
        number = number // 2
        binary_code.append(str(dig))
    binary_code = binary_code[::-1]
    return '-'.join(binary_code)


number = int(input("Please enter a number: "))
print('\nThe Binary code for ' + str(number) + ' is: ')
print(convert_binary(number))