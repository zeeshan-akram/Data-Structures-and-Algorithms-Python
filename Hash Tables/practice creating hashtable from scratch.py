class Hashtable:
    def __init__(self):
        self.linklist = [[] for _ in range(6)]

    def put(self, key, value):
        hash_key = hash(key) % len(self.linklist)
        self.insert(hash_key, key, value)

    def get(self, key):
        hash_key = hash(key) % len(self.linklist)
        result = self.look(hash_key, key)
        print(result)

    def delete(self, key):
        hash_key = hash(key) % len(self.linklist)
        result = self.remove(hash_key, key)
        print(result)


    def insert(self, hash_key, key, value):
        key_exist = False
        bucket = self.linklist[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                key_exist = True
        if key_exist:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def look(self, hash_key, key):
        bucket = self.linklist[hash_key]
        look = True
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                look = False
                return v
        if look:
            return f'{key} not Found'

    def remove(self, hash_key, key):
        bucket = self.linklist[hash_key]
        key_exist = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket.remove((k, v))
                key_exist = True
        if key_exist:
            return f'{key} deleted'
        else:
            return f'{key} not Found'

    def display(self):
        print(self.linklist)

linklist = Hashtable()
linklist.put(int(4), str('Bob'))
linklist.put(int(10), str('ali'))
linklist.put(int(9), str('zeeshan'))
linklist.get(1)
linklist.display()
linklist.delete(9)
linklist.display()