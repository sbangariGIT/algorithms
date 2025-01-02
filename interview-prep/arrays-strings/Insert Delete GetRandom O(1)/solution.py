import random

class RandomizedSet:

    def __init__(self):
        self.random_set = set()
        self.random_list = []
        self.random_map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.random_set.add(val)
        self.random_list.append(val)
        self.random_map[val] = len(self.random_list) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.random_set:
            return False
        self.random_set.remove(val)
        # swap the indexes and then update the swapped value
        last = self.random_list[-1]
        self.random_list[-1] = val
        self.random_list[self.random_map[val]] = last

        self.random_map[last] = self.random_map[val]
        del self.random_map[val]
        self.random_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_list)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()