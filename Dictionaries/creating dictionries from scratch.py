class LinkedList:
    def __init__(self):
        self.linklist = [[] for _ in range(6)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.linklist)
        key_exist = False
        bucket = self.linklist[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exist = True
        if key_exist:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.linklist)
        bucket = self.linklist[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.linklist)
        bucket = self.linklist[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket.remove(kv)
    def display(self):
        print(self.linklist)


dictionary = LinkedList()
dictionary.insert(int(5), str('Bob'))
dictionary.insert(int(1), str('Ali'))
dictionary.insert(int(0), str('umer'))
dictionary.display()
dictionary.delete(5)
dictionary.display()