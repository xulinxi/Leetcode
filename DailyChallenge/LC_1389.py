# 1389. Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        # Create an empty target array with the length of num 
        target = []
        
        # Since nums and index should have the same length, we just need one for loop
        for i in range(len(nums)):
            # list.insert() can push the item in the original position back
            target.insert(index[i],nums[i])

            # print(target)
            
        return target
        
        
