class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left to right and right to left loops -> accumulate products
        # need to have an additional array to store product and 
        # a variable to store accumulated product when going from right to left; 1[1,2,3,4]1

        res = [0] * len(nums)
        res[0] = 1
        R_accumulated = 1 # accumulating product from the right

        # [1,2,3,4] -> [1,1,2,6]
        for i in range(1, len(nums)):
            # accumulated product = prev one in res * prev num 
            res[i] = res[i-1] * nums[i-1] 

        # [1,1,2,6] -> [24,12,8,6]; R: 1, 1*4, 4*3, 12*2
        for j in range(len(nums)-1, -1, -1):
            res[j] = R_accumulated * res[j]
            R_accumulated = R_accumulated * nums[j]

        return res
