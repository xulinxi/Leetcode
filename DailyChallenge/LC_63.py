# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row_num = len(obstacleGrid)
        col_num = len(obstacleGrid[0])
        
        # If the starting cell has an obstacle, then simply return as there would be no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1
       
        
        # Filling the values for the first column
        for i in range(1, row_num):
            # print(int(False)) = 0
            # Note: obstacleGrid[i-1][0] == 1 => if the unit above current unit has a blockage, this unit is also blocked = 1
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
            
        # Filling the values for the first row
        for j in range(1, col_num):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
            
        # Startig from cell (1,1) fill up the values
        # Number of ways of reaching cell[i][j] = cell[i-1][j] + cell[i][j-1]
        # i.e. From above and left.
        for i in range(1, row_num):
            for j in range(1, col_num):
                # Note: Inside the first row and first row (don't include first row and first col), if the unit == 0, it means that there's no obstacle, so we can calculate the steps to reach here
                # ELSE: we encountered a 1, aka, blockage => change the step on the blockage to 0
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        # Return value stored in rightmost bottommost cell. This is the destination.
        return obstacleGrid[row_num-1][col_num-1]
        
        
        
        
        
        
        
        
        
        
        
        # ------------------incorrect
        # ****Note: (possible mistakes)
            # 1. Can't only set the blockage to 0, the units after the blockage should also set to be 0!
            
        
#         if obstacleGrid[0][0] == 1:
#             return 0
#         else:
#             row_num = len(obstacleGrid)
#             col_num = len(obstacleGrid[0])

#             for i in range(row_num):
#                 for j in range(col_num):
#                     if obstacleGrid[i][j] == 1:
#                         obstacleGrid[i][j] = 0
#                     else:
#                         obstacleGrid[i][j] = 1

#             # print(obstacleGrid)

#             for i in range(1, row_num):
#                 for j in range(1, col_num):
#                     if obstacleGrid[i][j] != 0:
#                             obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
#                     else:
#                         continue


#             # ****
#             return obstacleGrid[row_num-1][col_num-1]
        
