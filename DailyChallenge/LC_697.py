697. Degree of an Array

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # We first use dictionary to find out the degree of the nums list
#         nums_dict = {}
#         for num in nums:
#             if num not in nums_dict:
#                 nums_dict[num] = 1  
#             elif num in nums_dict:
#                 nums_dict[num] += 1
                
#         print(nums_dict)
#         degree = max(nums_dict, key = nums_dict.get)
#         # print(nums_dict, degree)

        # Note: we have to remember the index
        
        nums_dict, left, right = {}, {}, {}
        
        # store the position to left and right and store the count to nums_dict
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i
            # if x in left, and x appears again, we need to know the position of reappearing x
            right[x] = i
            
            nums_dict[x] = nums_dict.get(x, 0) + 1 # just equal to the code beneath:
#             if num not in nums_dict:
#                 nums_dict[num] = 1  
#             elif num in nums_dict:
#                 nums_dict[num] += 1

        ans = len(nums)
        degree = max(nums_dict.values()) # OR degree = max(nums_dict, key = nums_dict.get)
        
        # if a number has a matching degree, we calcualte the min length of this subarray
        for num in nums_dict:
            if nums_dict[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        
        return ans
                    
        
            
        
        
        
