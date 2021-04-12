# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for num in nums:
            # res = res ^ num
            res ^= num
            
        return res
            
