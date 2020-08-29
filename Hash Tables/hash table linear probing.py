class Hashtable:
    def __init__(self):
        self.array = [None for _ in range(5)]

    def put(self, key, value):
        hash_key = hash(key) % len(self.array)
        self.checkinsert(hash_key, key, value)

    def get(self, key):
        found = True
        result = self.find(found, key)
        print(result)

    def remove(self, key):
        result = self.checkremove(key)
        print(result)

    def size(self):
        size = 0
        for i in self.array:
            if i is not None:
                size += 1
        print(size)

    def display(self):
        print(self.array)

    def checkinsert(self, hash_key, key, value):
        condition = (hash_key + 1) % len(self.array)
        if self.array[hash_key] is None:
            self.array[hash_key] = (key, value)
        else:
            bucket = self.array[hash_key]
            if bucket[0] == key:
                self.array[hash_key] = (key, value)
            else:
                while condition != hash_key:
                    if self.array[condition] is None:
                        self.array[condition] = (key, value)
                        break
                    condition = (condition + 1) % len(self.array)

    def find(self, found, key):
        for i, kv in enumerate(self.array):
            if kv is not None:
                k, v = kv
                if k == key:
                    return v
                else:
                    found = False
        if found is False:
            return "Key not present"

    def checkremove(self, key):
        found = True
        for i, kv in enumerate(self.array):
            if kv is not None:
                k, v = kv
                if k == key:
                    removed = self.array[i]
                    self.array[i] = None
                    return f'{removed} removed'
                else:
                    found = False
        if found is False:
            return "Key not present"


linear = Hashtable()
linear.put(int(2), str('Bob'))
linear.put(int(3), str('Ali'))
linear.put(int(7), str('umer'))
linear.put(int(12), str('zeeshan'))
linear.display()
linear.get(12)
linear.remove(3)
linear.size()
