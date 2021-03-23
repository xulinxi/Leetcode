26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        temp_val = 0
        temp_val_index  = 0
        
        for i in range(len(nums)):
            temp_val = nums[temp_val_index]
            if nums[i] != nums[temp_val_index]:
                nums[temp_val_index + 1] = nums[i]
                temp_val_index += 1
        return temp_val_index + 1
                
        
