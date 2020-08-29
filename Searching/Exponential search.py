class JumpSort:
    def __init__(self):
        super().__init__()

    def exponentialSort(self, array, find):
        bound = 1
        while find > array[bound] and bound < len(array):
            bound += bound
        return self.__binarySearch(array, bound//2, bound, find)

    def __binarySearch(self, array, start, end, find):
        if start > end:
            return -1
        mid = (start + end) // 2
        if array[mid] == find:
            return mid
        if find > array[mid]:
            return self.__binarySearch(array, mid+1, end, find)
        if find < array[mid]:
            return self.__binarySearch(array, start, mid-1, find)


number = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30]
search = JumpSort()
print(search.exponentialSort(number, 20))
