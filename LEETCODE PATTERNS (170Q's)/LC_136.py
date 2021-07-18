# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Target: time: O(n); space: O(1)
        
        # Bit manupulation -> XOR (maybe clarify it using a formula/generic example)
        # num_once = nums[0]
        
        # 2 ^ 2 ^ 1 = 1
        # 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ 1 ^ 1 ^ 2 ^ 2 = 4
        
        
        # Initialize our num (appears once) w/ the first number in the array
        
                                    # input: [2,2,1]
        num_once = nums[0]          # num_once = nums[0] = 2
        # Iterate through the input array (Check: out of bound)
        for i in range(1, len(nums)):   # i = 2
            num_once ^= nums[i]             # num_once = num_once ^ nums[2] = 0 ^ 1 = 1
               
        return num_once                     # num_once = 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # (Scratches for Math) ---- Mine
# #         [2, 2, 1] len: 3; (3-1) / 2 = 2; with all numbers are duplicates (twice): [2, 2, 1, 1]
# #         [4,1,2,1,2] len: 5; (5-1) / 2; [4, 4, 1, 2, 1, 2,]



#         supposed_duplicate_value = 0
#         n = len(nums)
#         n_distinguish = (len(nums) - 1) // 2
        
#         for i in range(len)


        # # (Math) time: O(n); space: O(n) ---- Solution
        # unique_sum = sum(set(nums))
        # return 2 * unique_sum - sum(nums)



#         # (Bit Manipulation) time: O(n); space: O(1) ---- Mine
#         missing = nums[0]
    
#         for i in range(1, len(nums)):
#             missing ^= nums[i]
            
#         return missing
            
        
