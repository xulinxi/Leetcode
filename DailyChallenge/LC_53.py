class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # --------------------- Divide and Conquer-------------------------
        
#         def cross_Sum(nums, low, high, mid):
#             if low == high:
#                 return nums[low] 
            
#             left_subsum = float('-inf')
#             curr_sum = 0
#             # (Starting with the middle then move toward the first number)
#             # ***Note: low-1 because ending index is exclusive
#             for i in range(mid, low - 1, -1):
#                 curr_sum += nums[i]
#                 left_subsum = max(curr_sum, left_subsum)
            
#             right_subsum = float('-inf')
#             curr_sum = 0
#             # (Starting with the middle then move back)
#             for i in range(mid + 1, high + 1):
#                 curr_sum += nums[i]
#                 right_subsum = max(curr_sum, right_subsum)
                
#             return left_subsum + right_subsum
            
#         def helper_divCon(nums, low, high):
#             if low == high:
#                 return nums[low] 
            
#             mid = (high-low)//2 + low
#             left_sum = helper_divCon(nums, low, mid) 
#             right_sum = helper_divCon(nums, mid + 1, high) 
#             cross_sum = cross_Sum(nums, low, high, mid)
            
#             return max(left_sum, right_sum, cross_sum)
        
        
#         # *** return helper function to find the max sum
#         return helper_divCon(nums, 0, len(nums) - 1)
        
        
        
        # --------------Greedy-----------------------------
        answer = nums[0]
        total = nums[0]
        
        # Since we've stored index 0 value, we can just start from index 1
        # Mistake: for i in range(1, len(nums)-1): -> len(nums)-1 cannot be reached
        for i in range(1, len(nums)):
            total = max(total + nums[i], nums[i])
            answer = max(total, answer)
            
        return answer
