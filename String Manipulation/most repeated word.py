def mostRepeated(word):
    ASCII_VALUES = 256
    frequency = [0 for _ in range(ASCII_VALUES)]
    for ch in word:
        frequency[ord(ch)] += 1
    maximum = 0
    char = ' '
    for i in range(len(frequency)):
        if frequency[i] > maximum:
            maximum = frequency[i]
            char = chr(i)
    return char


print(mostRepeated('heloo'))
