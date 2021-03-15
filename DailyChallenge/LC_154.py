# 154. Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
# -----------------------------------TODO: Variant of Binary Search-----------------------------------
       
    
    
    
# ----------------Divide and Conquer/Recursion---------------(Exactly the same code from LC_153)

        lo, hi = 0, None

        # Create a helper function to find the min
        def min_finder(lo, hi):

            # Base case: if only one number left -> it's the min
            if lo == hi:
                return nums[lo]

            # If not the only one number left: call the helper function recursively
            # store the mininum number for each side via recursion
            mid = (hi - lo) // 2 + lo
            left_min = min_finder(lo, mid)
            right_min = min_finder(mid + 1, hi)


            return left_min if left_min < right_min else right_min

        return min_finder(0, len(nums) -1 )
        
        
        
        
        
# -----------_Brute Force----------------(Exactly the same code from LC_153)
        min = float('inf')
        for num in nums:
            if num < min:
                min = num

        return min
        
