# 213. House Robber II


class Solution:
    def rob(self, nums: List[int]) -> int:
        # check base case: - no house and only one house
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # helper function: t1, t2, temp (a value that stores past t1 , so we can update t2 to this number later)
        # This is a subfunction, we don't need "self": def robber_helper(self, nums: List[int]) -> int:
        def robber_helper(nums: List[int]) -> int:
            t1 = 0
            t2 = 0
            
            for current in nums:
                temp = t1
                t1 = max(t2 + current, t1)
                t2 = temp
              
            # *** t1 will keep calculating the max
            return t1
                

        # At the end, call the helper function.
        # *** return the max value when 1) start at the beginning (last house cannot be robbed) or the second house
        return max(robber_helper(nums[:-1]), robber_helper(nums[1:]))
