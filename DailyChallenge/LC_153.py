# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # When rotating, the direaction is going to the right like: --->; numbers moving to higher indices
        
        
        
        
        # -----------------Brute force------------------------
        min = float('inf')
        
        for num in nums:
            if num < min:
                min = num         
        return min
        
