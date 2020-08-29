class Sorting:
    def __init__(self):
        super().__init__()

    def countingSort(self, array):
        if len(array) == 0:
            return
        counting = [0 for _ in range(max(array)+1)]
        for num in array:
            counting[num] = array.count(num)
        self.__insert(array, counting)

    def __insert(self, array, counting):
        array.clear()
        for i in range(len(counting)):
            for _ in range(counting[i]):
                array.append(i)


numbers = [8, 4, 3, 5, 1, 2]
sort = Sorting()
sort.countingSort(numbers)
print(numbers)
