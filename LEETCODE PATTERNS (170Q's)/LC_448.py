# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        missing_nums = []
        nums_dict = {}
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
                
        for i in range(1, len(nums)+1):
            if i not in nums_dict:
                missing_nums.append(i)
                
        return missing_nums
