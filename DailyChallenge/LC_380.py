# 380. Insert Delete GetRandom O(1)


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Implement RandomizedSet using dictionary for O(1) time
        
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # Move the last element to the place index of the element to delete
            last_element, index = self.list[-1], self.dict[val]
            self.list[index], self.dict[last_element] = last_element, index
            
            # Delete the last element
            self.list.pop()
            del self.dict[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
