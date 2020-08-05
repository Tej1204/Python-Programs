def convert_to_five(value):
    num2 = 0
    for i in range(len(str(value))):
        dig = value % 10
        if dig == 0:
            dig = dig + 5
        value = value // 10
        dig = dig * 10 ** i
        num2 = num2 + dig
    print(num2)


value = int(input("Please enter a number: "))
convert_to_five(value)
