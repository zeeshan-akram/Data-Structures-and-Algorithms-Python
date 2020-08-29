class TernarySearch:
    def __init__(self):
        super().__init__()

    def ternary(self, array, find):
        start = 0
        end = len(array) - 1
        return self.__recursive(array, start, end, find)

    def __recursive(self, array, start, end, find):
        if start > end:
            return -1
        partition = (end - start) // 3
        mid1 = start + partition
        mid2 = end - partition
        if find == array[mid1]:
            return mid1
        if find == array[mid2]:
            return mid2
        if find > array[mid2]:
            return self.__recursive(array, mid2+1, end, find)
        if array[mid1] < find < array[mid2]:
            return self.__recursive(array, mid1+1, mid2-1, find)
        if find < array[mid1]:
            return self.__recursive(array, start, mid1-1, find)


number = [1, 4, 5]
search = TernarySearch()
print(search.ternary(number, 2))
