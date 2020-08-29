string = input('Enter sentence: ')
words = string.split(' ')
rev_string = ''
for i in range(len(words)-1, -1, -1):
    rev_string += words[i] + ' '
print(rev_string)
