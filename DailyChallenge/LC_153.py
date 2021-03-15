# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # When rotating, the direaction is going to the right like: --->; numbers moving to higher indices
        
        
        
# -----------------------------------TODO: Binary Search-----------------------------------
       
    
    
    
    # ----------------Divide and Conquer/Recursion----------------------------
        lo = 0
        hi = None
        
        def check_min(lo, hi):
            
            mid = (hi - lo) // 2 + lo
            
            # Base case: if only one number left -> it must be the smallest number
            if lo == hi:
                return nums[lo]
            
            # Remember the min in left and min in right
            left_min = check_min(lo, mid)
            right_min = check_min(mid + 1, hi)
            
            return left_min if left_min < right_min else right_min
            

        return check_min(lo, len(nums)-1)
        
        
        # -----------------Brute force------------------------
        min = float('inf')
        
        for num in nums:
            if num < min:
                min = num         
        return min
        
