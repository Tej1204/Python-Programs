# def convert_to_five(value):
#     num2 = 0
#     for i in range(len(str(value))):
#         dig = value % 10
#         if dig == 0:
#             dig = 5
#         value = value // 10
#         dig = dig * (10 ** i)
#         num2 = num2 + dig
#     return num2

def convert_to_five(value):
    value = str(value)
    converted_num = 0
    for i in range(len(value)):
        dig = int(value[i])
        if dig == 0:
            dig = 5
        converted_num = (converted_num * 10) + dig
    return converted_num


value = int(input("Please enter a number: "))
print(convert_to_five(value))
