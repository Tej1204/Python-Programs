def reverse_string(word):
    mylist = []
    for i in range(1, len(word) + 1):
        mylist.append(word[-i])
    return ''.join(mylist)


word = input("Enter a word: ")
new_word = reverse_string(word)
if word == new_word:
    print('\n' + word + ' is a palindrome')
else:
    print('\n' + word + ' is not a palindrome')
    print('The opposite of ' + word + ' is ' + new_word)


