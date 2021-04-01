# 170. Two Sum III - Data structure design


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_structure = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.data_structure:
            self.data_structure[number] = 1
        elif number in self.data_structure:
            self.data_structure[number] += 1
        
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        
        # Note: need to remember if the complete == num
        
        for num in self.data_structure.keys():
            complete = value - num
            if complete != num:
                if complete in self.data_structure:
                    return True
            if complete == num:
                if self.data_structure[complete] > 1:
                    return True
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
