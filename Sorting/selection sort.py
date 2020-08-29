class Sorting:
    def __init__(self):
        super().__init__()
        self.array = []

    def insert(self, items):
        for item in items:
            self.array.append(item)

    def selectionSort(self):
        for index in range(len(self.array)):
            minimum = self.__getMinimum(index)
            if index != minimum:
                self.__swap(index, minimum)

    def display(self):
        print(self.array)

    def __getMinimum(self, index):
        min_index = index
        minimum = self.array[index]
        for i in range(index, len(self.array)):
            if minimum > self.array[i]:
                minimum = self.array[i]
                min_index = self.array.index(self.array[i])
        return min_index

    def __swap(self, index_1, index_2):
        self.array[index_1], self.array[index_2] =\
            self.array[index_2], self.array[index_1]


numbers = [8, 2, 4, 1, 3]
sort = Sorting()
sort.insert(numbers)
sort.selectionSort()
sort.display()