# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Use two for loop to add up each combination once
        
        # Only need to loop until n-1 index since the last pair is the last two numbers
        for i in range(len(nums) - 1):
            # We don't need to check the numbers that the first loop has walked through 
            # Therefore, the number of j we need to check decreases while i increase: 
            # when i = 0, we check 3 numbers in j
            # when i = 1, we check 2 numbers in j
            # Thus, the len of round in j: len(List) - 1 - i
            # j starts with the number after i: j = i + 1
            for j in range(len(nums) - 1 - i):
                if nums[i] + nums[j + i + 1] == target:
                    return[i, j + i + 1]
                
