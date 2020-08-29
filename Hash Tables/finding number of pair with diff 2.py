dict = {}
array = [1, 7, 5, 9, 2, 12, 3]
count = 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if abs(array[i]-array[j]) == 2:
            dict[count] = f'{array[i]},{array[j]}'
            count += 1
print(len(dict))