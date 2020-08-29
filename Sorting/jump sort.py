class JumpSort:
    def __init__(self):
        super().__init__()

    def jumpSort(self, array, find):
        return self.__jumpSort(array, find)

    def __jumpSort(self, array, find):
        bucket = int((len(array)) ** 0.5)
        start = 0
        end = bucket
        limit = len(array)
        while find > array[end - 1] and start < limit:
            start = end
            end += bucket
            if end > limit:
                end = limit
                break
        for i in range(start, end):
            if find == array[i]:
                return i
        return -1


number = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30]
search = JumpSort()
print(search.jumpSort(number, 30))
