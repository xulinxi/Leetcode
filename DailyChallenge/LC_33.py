33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
#         # ------O(n); brute force-----------------
#         for num_index in range(len(nums)):
#             if nums[num_index] == target:
#                 return num_index
            
#         return -1
    
    # -----------O(log n) --------------------------------(needs more practice): Iterative and Recursive
        if not nums:
            return -1
        
        def binary_search_recur(low, high):

            if low > high: # Prevent the case when high becomes less than low
                return -1
            mid = (high-low)//2 + low
            
            if nums[mid] == target: 
                return mid
            if nums[low] <= target < nums[mid]: # Checking if the target falls between [low, mid] range
                return binary_search_recur(low, mid-1)
            elif nums[mid] < target <= nums[high]:
                # *** Alway remember your return statement
                return binary_search_recur(mid + 1, high)
            elif nums[mid] > nums[high]: # ***Found the pivot point ex: [7,0] in the list -> check right (leftside in a sorted list)
                return binary_search_recur(mid + 1, high)
            else: # ***Found the pivot point ex: [7,0] in the list -> check left (rightside (greater elements) in a sorted list)
                return binary_search_recur(low, mid-1)
                
        return binary_search_recur(0, len(nums)-1)
            
        
    
    
    
