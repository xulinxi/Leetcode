# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        
        
        # (Hashmap) time: O(n); space: O(n) ---- Solution
        count, sums = 0, 0
        
        # key = sums - k; when we find a range of sum == k -> update count +=1 
        d = {0:1}
        
        for i in range(len(nums)):
            sums += nums[i]
            
            # if sums-k == 0; update count += 1
            # if sums-k < 0; get 0
            # if sums-k > 0; find sums-k in dict: (means we can get to k after substracting the number before we get to this sums) -> find another way
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
            
        return count
        
