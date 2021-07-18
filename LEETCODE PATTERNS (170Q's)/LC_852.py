# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
#         # (Linear Scane) time: O(n); space(1); ----Mine
#         # Goal: Find max
        
#         peak = 0
        
#         for i in range(1, len(arr)):
#             if arr[i] > arr[peak]:
#                 peak = i
                
#         return peak


        # (Binary Search) time: O(logn); space(1) ---- Solution
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] < arr[mid + 1]: # at left side of the mountain -> move to the right part
                low = mid + 1
            else:  # arr[mid] > arr[mid + 1]: at right side of the mountain -> move left
                high = mid
            
        # return low/high doesn't matter -> will be equal at the end -> review binary search!
        return high
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
