import random

class MyHashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.collisions = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        h = self._hash(key)
        bucket = self.buckets[h]
        if len(bucket) > 0:
            self.collisions += 1
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

keys = [f"key_{i}" for i in range(1000)]
for size in [100, 500, 1000, 2000]:
    table = MyHashTable(size)
    for k in keys:
        table.put(k, random.randint(1, 100))
    print(f"Розмір таблиці: {size} | Колізій: {table.collisions}")