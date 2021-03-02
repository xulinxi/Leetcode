# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for i in range(len(nums)):
            
            # Create a count to keep track of how much numbers in the array are smaller than it
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            result.append(count)
            
        return result


        # Another way with counting sort algorithm can also be implemented.
