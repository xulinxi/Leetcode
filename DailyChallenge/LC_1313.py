# 1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        # Create a list for each pair, and then concatenate them together
        result_list = []
        
        # Because we only need the index of first half, we only need the length of half nums list (O(logn))
        # "/" is for float object
        for i in range(len(nums)//2):
            result_list = result_list + [nums[i*2+1]]*(nums[i*2])
            print(nums[i*2+1],nums[i*2])
        
        return result_list
    
    # Note: make sure remember to use the number that set on the index, instead of using the index!
    # *** Return the results outside of for loop.

        
