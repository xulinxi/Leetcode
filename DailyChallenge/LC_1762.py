# 1762. Buildings With an Ocean View

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # Goal: Find the indexes of the numbers that are greater than the numbers at their (targeted numbers) right hand sides. 
        # time: O(n); space: O(1)
        
        # *** we know the last building is always ocean view
        ocean_view = [len(heights)-1]
        max_h = heights[len(heights)-1]
        
        # Iterate through through the list from the second to the last building to the first building
            # - updating the max_height/max_h (if we found a bulding that's higher than all of the buildings at its right hand side)
            
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_h:
                max_h = heights[i]
                ocean_view.append(i)
                
        # heights = [4,2,3,1] 
        # ocean_view = [3, 2, 0] -> [0, 2, 3]
            
        ocean_view.reverse()
        
        return ocean_view
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Goal: Find the indexes of the numbers that are greater than the numbers after them
#         curr_max = heights[len(heights) - 1]   # 1
#         ocean_view = [len(heights) - 1]
        
#         pointer = len(heights) - 2    # 2
        
#         while pointer >= 0:  # 2, 1, 0
#             if heights[pointer] > curr_max:
#                 ocean_view.append(pointer)
#                 curr_max = heights[pointer]
#             pointer -= 1
        
#         ocean_view.reverse()
        
#         return ocean_view
