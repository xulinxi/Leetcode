# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # -------------------------#TODO: Divide and Conquer--------------------
        
        
        
        
        # -----------------_Sliding Window:------------
        answer = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            # total is recording the maximun sum from past numbers
            total = max(nums[i], nums[i]+total)
            
            answer = max(total, answer)
            # if total > answer:
            #     answer = total
                
        return answer
        
        
        
        
        
        
        # -----------Brute Force----------------(Wrong answer)
#         max_sum = float('-inf')
#         lo, hi = 0, 0
        
#         # If only one number exists in the list
#         if len(nums) == 1:
#             return nums[0]
        
#         # Else: more than one item in the list
#         for lo in range(len(nums)):
#             temp_sum = 0
#             temp_sum += nums[lo]
#             # check if each number can has the largest sum
#             max_sum = max(max_sum, temp_sum)
            
#             # add the hi (end of the window to the sum)
#             for hi in range(len(nums)):
#                 temp_sum += nums[hi]
#                 max_sum = max(max_sum, temp_sum)
                
#         return max_sum
                
            
            
            
            
            
            
            
            
            
