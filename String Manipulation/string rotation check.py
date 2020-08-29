def rotationCheck(word, reverse):
    return len(word) == len(reverse) and reverse in (word + word)


print(rotationCheck('ABCD', 'ADBC'))
