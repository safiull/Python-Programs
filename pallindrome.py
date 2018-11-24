word = (input('please enter your word: '))
word = word.casefold()
reversed_word = word[::-1]
if word == reversed_word:
    print('Yes, this is pallindrome')
else:
    print("LOL, this is not a pallindrome")