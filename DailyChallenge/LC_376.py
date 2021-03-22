# 376. Wiggle Subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        # -------------Answers from Eric:--------------
        res_len = 1
        up = None
        
        for i in range(1, len(nums)):
            # Wrong: if nums[i] > nums[i-1] and not up: (None is not True)
            if nums[i] > nums[i-1] and up != True:
                res_len += 1
                up = True
            # Wrong: if nums[i] < nums[i-1] and up: (None is not False)
            if nums[i] < nums[i-1] and up != False: 
                res_len += 1
                up = False   
                
        return res_len
            
        # ------------In Progress-------------(Mine)
#         if len(nums) < 2:
#             return 1
        
#         if len(nums) > 1:
#             current = nums[0]
#             next = nums[1]
#             bool_check = True
#             curr_i = 0
#             next_i = 1
#             diff_curr = nums[next_i] - nums[curr_i]
            
            
            
#             while bool_check:
#                 curr_i += 1
#                 next_i += 1
#                 diff_curr = nums[next_i] - nums[curr_i]
#                 if (diff_curr < 0  and diff_next > 0) or (diff_curr > 0  and diff_next < 0):
#                     diff_curr = diff_next
#                     bool_check = True
#                     continue
#                 else:
#                     del nums[i + 1]
#                     diff_next = nums[i+1] - nums[i]
#                     bool_check = False
                    
#         return len(nums)
                    
                
            
            
            
            
    
        
