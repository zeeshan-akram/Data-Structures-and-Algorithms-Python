class Sorting:
    def __init__(self):
        super().__init__()

    def bucketSort(self, array, n):
        bucket = [[] for _ in range(n)]
        for num in array:
            ind = num // len(bucket)
            bucket[ind].append(num)
        self.__bucketsSorting(array, bucket)

    def __bucketsSorting(self, array, bucket):
        i = 0
        for buck in bucket:
            buck.sort()
            for item in buck:
                array[i] = item
                i += 1


numbers = [6, 2, 5, 4, 3, 7]
sort = Sorting()
sort.bucketSort(numbers, 3)
print(numbers)