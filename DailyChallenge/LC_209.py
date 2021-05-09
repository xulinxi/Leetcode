# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#
        
        # ------------O(n)
        ans = float("inf")
        target_sum = 0
        left = 0
        
        for i in range(len(nums)):
            
            target_sum += nums[i]
            while target_sum >= target:
                ans = min(ans, i - left + 1)
                target_sum -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
        
        
        
        
            
