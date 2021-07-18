# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # (Dynamic Programming, Kadane's Algorithm) time: O(n); space: O(1) ---- Solution
        
        # Initialize our variables using the first element.
        current_subarray_sum = max_subarray_sum = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray_sum = max(num, current_subarray_sum + num)
            max_subarray_sum = max(max_subarray_sum, current_subarray_sum)
        return max_subarray_sum
        
        
        
        
        
#         # WRONG (One Path) time: O(n); space: O(1) ---- Mine
#         if len(nums) == 1:
#             return nums[0]
        
#         else:
#             # Mistake: max_sum = float("-inf"); won't be correct for [-1, -2] 
#             max_sum = nums[0]
#             current_sum = nums[0]

#             for i in range(1, len(nums)):
#                 if current_sum < nums[i]:
#     #                 current_sum = nums[i] Note: here should be current_sum = max(nums[i], current_sum + num[i])
#                     current_sum = max(nums[i], current_sum + nums[i])    
#                 else:
#                     current_sum += nums[i]
#                     max_sum = max(current_sum, max_sum)

#             return max_sum
            
        
        
        
        
