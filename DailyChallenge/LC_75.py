# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize the pointers (index):
        #     p0: 0 because for all index < p0: nums[index < p0] = 0
        #     curr: index of the element under consideration (currently)
        #     p2: len(nums) - 1 becase for all index > p2: nums[index > p2] = 2
        p0, curr = 0, 0
        p2 = len(nums)-1
        
        while curr <= p2:
            # if most recent number we check is 0, we update the boundary
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
                
            # use elif in this case because if the previous statement is executed, curr will be changed
            # if most recent number we check is 2, we swap the values at curr and p2, and move left
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -=1
                
            else:
                curr += 1
                
        
        
        
