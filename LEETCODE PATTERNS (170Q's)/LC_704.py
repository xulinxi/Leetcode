# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
    # (Iterative) time: log(n); space: O(1) ---- Solution
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        # Bug: migging check for null target case
        # **** what if no target? -> return -1
        return -1
        
    
#     # (Recursive) time: log(n); space: O(1) ---- Ojaswa
    
#     def search(self, nums: List[int], target: int) -> int:
#         return self.bsearch(nums, target, 0, len(nums)-1)
        
#     def bsearch(self, nums, target, low, high):
#         if high < low:
#             return -1
#         mid = low + (high - low) // 2
        
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             return self.bsearch(nums, target, low, mid - 1)
#         else:
#             return self.bsearch(nums, target, mid + 1, high)
        
        
        
#         # Wrong (Recursive) ---- Mine
#         # Bugs: needs to put in a range (low, high, mid)
#         if len(nums) == 1:
#             return 0
        
#         else:
#             mid = len(nums) // 2
#             if nums[mid]  == target:
#                 return mid
#             elif nums[mid] > target:
#                 return search(nums[:mid-1], target)
#             else:
#                 return search(nums[mid+1:], target)
