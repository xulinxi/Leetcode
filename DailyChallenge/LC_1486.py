# 1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        # Compute the nums array, and use bitwide XOR on all num in that array.
        nums = [0] * n
        for i in range(n):
            # (lol leetcode even provides the code for generating this nums array.)
            nums[i] = start + 2 * i
        
        result = 0
        
        for num in nums:
            result = result ^ num
        
        return result
