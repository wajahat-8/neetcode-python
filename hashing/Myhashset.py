class MyHashSet:
    def __init__(self):
        self.SIZE = 10007
        self.hashSet = [None] * self.SIZE

    def hashing(self, key):
        return key % self.SIZE

    def add(self, key):
        index = self.hashing(key)
        while self.hashSet[index] is not None and self.hashSet[index] != key:
            index = (index + 1) % self.SIZE
        self.hashSet[index] = key

    def remove(self, key):
        index = self.hashing(key)
        while self.hashSet[index] is not None:
            if self.hashSet[index] == key:
                self.hashSet[index] = -2
                return
            index = (index + 1) % self.SIZE

    def contains(self, key):
        index = self.hashing(key)
        while self.hashSet[index] is not None:
            if self.hashSet[index] == key:
                return True
            index = (index + 1) % self.SIZE
        return False

# Test code (no indentation here)
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))  # True
print(obj.contains(3))  # False
obj.add(2)
print(obj.contains(2))  # True
obj.remove(2)
print(obj.contains(2))  # False
