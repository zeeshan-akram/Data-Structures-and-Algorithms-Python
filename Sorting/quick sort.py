class Sorting:
    def __init__(self):
        super().__init__()

    def quickSort(self, array):
        self.__quickSort(array, start=0, end=len(array)-1)

    def __quickSort(self, array, start, end):
        if start >= end:
            return
        boundary = self.__partition(array, start, end)
        self.__quickSort(array, start, boundary-1)
        self.__quickSort(array, boundary+1, end)

    def __partition(self, array, start, end):
        pivot = array[end]
        boundary = start - 1
        for i in range(start, end+1):
            if array[i] <= pivot:
                boundary += 1
                self.__swap(array, i, boundary)
        return boundary

    def __swap(self, array, index_1, index_2):
        array[index_1], array[index_2] =\
            array[index_2], array[index_1]


numbers = [8, 2, 4, 1, 3]
sort = Sorting()
sort.quickSort(numbers)
print(numbers)
