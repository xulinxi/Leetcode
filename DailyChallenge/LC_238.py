# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
#         nums = 1 [1,2,3,4] 1
#     i   num    ans[i]
#     0    1       2 * 3 * 4
#     1    2   1 *     3 * 4      
#     2    3   1 * 2 *     4
#     3    4   1 * 2 * 3  
    
        
        
#                [24,12,8,6]
            
#                                      R = 1 * 4 * 3 * 2
#         2 loops           1 [1,2,3,4] 1     

#         1st loop answer [1, 1, 2, 6]
        
#         2nd loop answer [24, 12, 8, 6]
                        
#                         answer[i] * R
                
#         time: O(2n) = O(n); space: O(1)




#         input: nums = [2,2,3,4]
                        # [24, 24, 16, 12]
        

        ans = [0] * len(nums)    # [0, 0, 0, 0]
        
        # Accumulating all products of the numbers at the left hand side
        ans[0] = 1     # ans [1, 0, 0, 0]
        
        # 1st loop: (all left products)
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        # print(ans)
            
        # end of for 1st loop: [1, 2, 4, 12]
        
        # 2nd loop: (all right products)
        R = 1
        
        for j in range(len(ans)-1, -1, -1):
            ans[j] = ans[j] * R  # [24, 24, 16, 12]
            R *= nums[j]     # R = 1 * 4 = 4 *3 = 48
            
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # (O(1) space approach) time: O(n); space: O(1) ---- Solution
        
#         answer = [0] * len(nums)
        
#         # answer[i] contains the product of all the elements to the left
#         # Note: for the element at index '0', there are no elements to the element, to the answer[0] = 1
#         answer[0] = 1
        
#         for i in range(1, len(nums)):
            
#             # answer[i-1] already contains the product of elements to the left of 'i-1'
#             # Simply multiplying it with nums[i-1] would give the product of all
#             # input: [1,2,3,4]
#             # answer [1,1,2,6]
            
#             answer[i] = nums[i-1] * answer[i-1]
            
#         # R contains the product of all the element to the right
#         # Note: for the element at index 'length - 1/ len(nums) - 1', there are no elements to the right
#         R = 1
        
#         # Correct: for i in reversed(range(len(nums))):
#         # BUG: for i in range(len(nums), -1, -1):
#         for i in range(len(nums)-1, -1, -1):
#             # print(i)
#             # For the index 'i', R would contain the product of all elements to the right.
#             # input: [1,2,3,4]
#             # answer [24,12,8,6]
            
#             answer[i] = answer[i] * R
#             R *= nums[i]
            
#         return answer
            
        
    
    
    
            
        
    
