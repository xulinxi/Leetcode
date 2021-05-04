# 665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0

        for i in range(1, len(nums)):
            # ****Mistake:之前也遇见过，once the count == 2 and the list reaches the end, it doesn't go through this statement anymore 
            # -> we can bring this check statement outside of the for loop
            # if  count > 1:
            #     return False
            if nums[i-1] > nums[i] :
                
                # Added steps: 
                # If we've encourted violation, with this violation, we has more than 1 violation. Hence, return False
                if count == 1:
                    return False
                
                count += 1
                
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                         
                # We modify the first violation and continue checking if there's more violation
                else: nums[i] = nums[i - 1]
        # if count > 1:
        #     return False
        return True
