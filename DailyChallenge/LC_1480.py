# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
# no need to do recursion, just calculate sum for each index in the final array/list and put then in the final array/list
        index_sum = 0
        result = []
        for i in range(len(nums)):
            index_sum = index_sum + nums[i]
            # print(nums[i], index_sum)
            result.append(index_sum)
            
        return result
