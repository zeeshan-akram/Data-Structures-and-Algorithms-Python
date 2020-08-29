def linearSearch(array, find):
    index = -1
    for i in range(len(array)):
        if find == array[i]:
            index = i
            break
    if index != -1:
        print(f'found at index: {index}')
    else:
        print('Not found')


numbers = [2, 4, 5, 8, 2, 1]
linearSearch(numbers, 1)
