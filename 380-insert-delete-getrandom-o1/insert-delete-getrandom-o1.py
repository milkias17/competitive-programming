import random 

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        exists = val in self.map
        if not exists:
            self.map[val] = len(self.arr)
            self.arr.append(val)
        return not exists

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        last = len(self.arr) - 1
        idx = self.map[val]

        self.map[self.arr[last]] = idx
        self.arr[last], self.arr[idx] = self.arr[idx], self.arr[last]
        self.arr.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        val = random.choice(self.arr)
        return val

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()