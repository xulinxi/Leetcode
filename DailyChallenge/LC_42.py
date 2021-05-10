# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        maxL, maxR = height[0], height[-1]
        trappedWater = 0
        
        # Initialize 2 pointers
        left, right = 1, len(height) - 2
        
        # As long as left and right pointers are not crossed:
        while left <= right:
            
            # Check 1: which max is greater
            # (-if min(maxL, maxR) = maxL)
            if maxL < maxR: 
                # Check 2: (current vs. max) Check while traversing: Update maxL while traversing
                # Check 2: - if curr > max: update max with curr
                # - if curr < max: calculate the trapped water within the curr
                if height[left] >= maxL:
                    maxL = height[left]
                    
                # (Update the amount of trappedWater)   
                else:
                    trappedWater += maxL - height[left]
                # Update pointer index
                left += 1
            
            # -if min(maxL, maxR) = maxR   
            else:
                # Check 2
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    trappedWater += maxR - height[right]
                right -= 1
                
        return trappedWater
                
        
        
        
