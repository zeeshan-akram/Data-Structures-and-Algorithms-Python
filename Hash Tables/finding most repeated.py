dict = {}
array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
for n in array:
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] = dict[n] + 1
most_repeated = 0
for key in dict.keys():
    if dict[key] > most_repeated:
        most_repeated = key

print(most_repeated)