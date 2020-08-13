# def reverse_string(word):
#     mylist = []
#     i = -1
#     while word != '':
#         let = word[i]
#         mylist.append(let)
#         i = i - 1
#     return ''.join(mylist)

def reverse_string(word):
    mylist = []
    for i in range(1, len(word) + 1):
        mylist.append(word[-i])
    return ''.join(mylist)


word = input("Enter a word: ")
print(reverse_string(word))
