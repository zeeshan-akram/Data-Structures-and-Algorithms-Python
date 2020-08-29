class Sorting:
    def __init__(self):
        super().__init__()
        self.array = []

    def insert(self, items):
        for item in items:
            self.array.append(item)

    def mergeSort(self):
        self.array = self.__mergeSort(self.array)

    def display(self):
        print(self.array)

    def __mergeSort(self, array):
        if len(array) == 1:
            return array
        middle = len(array) // 2
        left_array = array[0:middle]
        right_array = array[middle:len(array)]
        left_array = self.__mergeSort(left_array)
        right_array = self.__mergeSort(right_array)
        return self.__mergeArrays(array, left_array, right_array)

    def __mergeArrays(self, array, left_array, right_array):
        left_ind = 0
        right_ind = 0
        mini = 0
        for index in range(len(array)):
            if len(left_array) == left_ind:
                mini = right_array[right_ind]
                right_ind += 1
            elif len(right_array) == right_ind:
                mini = left_array[left_ind]
                left_ind += 1
            elif left_array[left_ind] > right_array[right_ind]:
                mini = right_array[right_ind]
                right_ind += 1
            elif left_array[left_ind] < right_array[right_ind]:
                mini = left_array[left_ind]
                left_ind += 1
            array[index] = mini
        return array


numbers = [8, 2, 4, 1, 3]
sort = Sorting()
sort.insert(numbers)
sort.mergeSort()
sort.display()
