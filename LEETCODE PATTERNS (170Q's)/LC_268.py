# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Dictionary(key, value) / Set; time: O(2n) = O(n); space: set => O(n)
        # 1. Iterate through the input array (nums) -> store each value into a set (for loop)
        # 2. len(nums); [0, 1, 2 ... n]; ex: nums = [3,0,1]; [0, 1, 2, 3, 4] (for loop)
            # for i in range(len(nums) + 1)
            # if i not in the set:
                # return i
             
        
        # missing = len(nums) = 3;
        
        # missing = missing ^ 3 ^ 0 ^ 1 ^ 0 ^ 1 ^ 2 = > 3 ^ 3 ^ 0 ^ 0 ^ 1 ^ 1 ^  2 = 2
        # for i in range(len(nums)):
            # missing ^= nums[i] ^ i
        
        # [0, 1, 2] [0, 1, 2, 3]
         # 3 ^ 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 2 = 3
            
        # Initialize missing with the len
        missing = len(nums) # missing = 2
        
        # XOR each number in the input array with the supposed value
        for i in range(len(nums)): # i: 0, 1
            missing ^= nums[i] ^ i # missing = 2 ^= 0 ^ 0 = 2; 2 ^= 1 ^ 1 = 2
            
        return missing
            
        # space: O(1); time: O(n)
        
        
        # Another method: (hack)
           # (sum of what it supposed to be) - (sum up the amount)


            
        
                
        
                
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # (Bit Manipulation) time: O(n); space: O(1) ---- Solution
        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing ^= i ^ num
        # return missing
        
        
        
        
        
    
        
        
        
#         # (Hash Map/Dictionary) time: O(n); space O(n) ---- Mine
#         storingSet = set()
        
#         # Note: Be careful with the end index
#         for i in range(len(nums)):
#             # print(type(nums[i]))
#             storingSet.add(nums[i])
            
#         # Note: Be careful with the end index
#         for i in range(len(nums) +1):
#             if i not in storingSet:
#                 # print(type(i), type(nums[i]))
#                 # print(i, nums)
#                 return i
            
            # # ----Solution
            # num_set = set(nums)
            # n = len(nums) + 1
            # for number in range(n)
            #     if number not in num_set:
            #         return number
            
            
            
    
            
    
            
            
            
