class Sorting:
    def __init__(self):
        super().__init__()

    def bubbleSort(self, array):
        for i in range(len(array)):
            if self.__isSorted(array):
                break
            else:
                for index in range(len(array)-1):
                    if array[index] > array[index + 1]:
                        self.__swap(array, index, index + 1)

    def __isSorted(self, array) -> bool:
        minimum = array[0]
        for num in array:
            if num < minimum:
                minimum = num
                break
        return True if minimum == array[0] else False

    def __swap(self, array, index_1, index_2):
        array[index_1], array[index_2] =\
            array[index_2], array[index_1]


numbers = [8, 2, 4, 1, 3]
sort = Sorting()
sort.bubbleSort(numbers)
print(numbers)
