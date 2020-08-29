class BinarySearch:
    def __init__(self):
        super().__init__()

    def binary(self, array, find):
        start = 0
        end = len(array) - 1
        return self.__recursive(array, start, end, find)

    def binaryIterative(self, array, find):
        index, mid = self.__iterative(array, find)
        if index != mid:
            print('Not Found')
        else:
            print("Found at :", index)

    def __iterative(self, array, find):
        start = 0
        end = len(array) - 1
        index = mid = (start + end) // 2
        while start != mid:
            if array[mid] == find:
                index = mid
                break
            elif find < array[mid]:
                end = mid
            elif find > array[mid]:
                start = mid
            mid = (start + end) // 2
        return index, mid

    def __recursive(self, array, start, end, find):
        if start > end:
            return -1
        mid = (start + end) // 2
        if array[mid] == find:
            return mid
        if find < array[mid]:
            return self.__recursive(array, start, mid-1, find)
        if find > array[mid]:
            return self.__recursive(array, mid+1, end, find)


number = [1]
search = BinarySearch()
print(search.binary(number, 1))
