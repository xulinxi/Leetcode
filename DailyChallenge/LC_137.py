# 137. Single Number II

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # (Hashmap)-----------------------------------------
#         dictionary = Counter(nums)
        
#         for k in dictionary:
#             if dictionary[k] == 1:
#                 return k
        
        
# ---------------------------------------------------------Bitwise
        # initialize seen_once and seen_twice = 0
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance:
                # add num to seen_once
                # don't add to seen-twice because of presence in seen_once
                
            # second appearance:
                # remove num from seen_once
                # add num to seen_twice
                
                
            # third appearance:
                # don't add to seen_once because of presence in seen_twice
                # removenum from seen_twice
                
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
            
        return seen_once
            
