class MyHashMap:
    SIZE = 10007
    EMPTY = -1
    DELETED = -2

    def __init__(self):
        self.keys = [self.EMPTY] * self.SIZE
        self.values = [0] * self.SIZE

    def hashing(self, key):
        return key % self.SIZE

    def put(self, key, value):
        index = self.hashing(key)
        while self.keys[index] != self.EMPTY and self.keys[index] != self.DELETED and self.keys[index] != key:
            index = (index + 1) % self.SIZE
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hashing(key)
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.SIZE
        return -1

    def remove(self, key):
        index = self.hashing(key)
        while self.keys[index] != self.EMPTY:
            if self.keys[index] == key:
                self.keys[index] = self.DELETED
                return
            index = (index + 1) % self.SIZE


# Testing the class
my_map = MyHashMap()

my_map.put(1, 10)
my_map.put(2, 20)
my_map.put(10200, 30)  # Intentional collision

print(my_map.get(1))      # Output: 10
print(my_map.get(2))      # Output: 20
print(my_map.get(10200))  # Output: 30
print(my_map.get(3))      # Output: -1 (not found)

my_map.remove(2)
print(my_map.get(2))      # Output: -1 (after removal)
