# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # jumps that we need to take
        jumps = 0
        # At current position, the steps that this jump takes
        current_jump_end = 0
        # the farthest we can go for this jump
        farthest = 0
        
        # Note: len(nums) - 1: prevent us to make a jump at the last step
        for i in range(len(nums) - 1):
            
            # we continuously find how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            
            # if we have come to the end of the current jump, we need to make another jump
            # Note: when we reach the last step of the jump (not end of the array)
                # -> we are ready to start the next jump and add this next jump to the count
                # -> we update the next current_jump_end with the farthest step we found
            if i == current_jump_end:
                
                # record down the number of jumps
                jumps += 1
                current_jump_end = farthest
                
        return jumps
