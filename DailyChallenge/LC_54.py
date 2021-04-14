# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # --------------Simulation
        
        if not matrix: return []
        
        R, C = len(matrix), len(matrix[0])
        
        seen = [[False] * C for _ in matrix]
        ans = []
        # dr: direction of row; dc: direction of col;
        # Top: dr[0]=0, dc[0]=1 -> (0,1) -> when row doesn't change, but col is changing
        # [top, right, bottom, left]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            
            # cr: current row; cc: current col
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c, = cr, cc
                
            # if reaches the end of the row or col, we need to switch a direction
            else:
                # we have 4 directions
                di = (di + 1) % 4
                # Switch direction and the new starting r, c in the new direction
                r, c = r + dr[di], c + dc[di]
        
        return ans
        
        
        
        
        
    
        
        
        # ------------------Layer-by-Layer
#         def spiral_coords(r1, c1, r2, c2):
            
#             # Top: Every coordinate in top row (row1 stays the same, while column index changes)
#             for c in range(c1, c2 + 1):
#                 yield r1, c
                
#             # Right: Every coordinate in right side (c2 stays the same, but don't append the first number in c2 (has qppended in the prvious for loop; therefore starts with r1 + 1 -> r2 + 1 ))   
#             for r in range(r1 + 1, r2 + 1):
#                 yield r, c2
                
#             # To avoid appending duplicates, we only need to go through the bottom and 
#             if r1 < r2 and c1 < c2:
#                 # Bottom: Counting backward ->All coordinates except the bottom rightest coordinate 
#                 for c in range(c2 - 1, c1, -1):
#                     yield r2, c
                
#                 # Left: 
#                 for r in range(r2, r1, -1):
#                     yield r, c1
                    
#         if not matrix: return []
#         ans = []
#         r1, r2 = 0, len(matrix) - 1
#         c1, c2 = 0, len(matrix[0]) - 1
        
#         while r1 <= r2 and c1 <= c2:
#             for r, c, in spiral_coords(r1, c1, r2, c2):
#                 ans.append(matrix[r][c])
                
#             r1 += 1
#             r2 -= 1
            
#             c1 += 1
#             c2 -= 1
            
#         return ans
