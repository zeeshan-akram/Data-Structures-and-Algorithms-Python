class InsertingSorting:
    def __init__(self):
        super().__init__()

    def insertionSort(self, array):
        sorting = []
        for item in array:
            index = self.__getIndex(item, sorting)
            sorting.insert(index, item)
        return sorting

    def __getIndex(self, item, sorting):
        index = 0
        if len(sorting) == 0:
            index = 0
        else:
            for ind in sorting:
                if item < ind:
                    index = sorting.index(ind)
                    break
                elif item > ind:
                    index += 1
        return index


#numbers = [6, 7, 5, 2, 1]
#sort = InsertingSorting()
#numbers = sort.insertionSort(numbers)
#print(numbers)
