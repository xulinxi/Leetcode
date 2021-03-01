# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
#         Create a result list
        result = []
    
#     Add in each value in order

        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        
        return result
        
#         Note: read the question carefully! Map out thought process first.
