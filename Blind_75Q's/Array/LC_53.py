class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if curr_sum < curr_num -> curr_sum should be set to curr_num

        curr_sum, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            curr_num = nums[i]
            curr_sum = curr_sum + nums[i]

            if curr_sum < curr_num:
                curr_sum = curr_num
            
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
            

