# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # row_num = len(grid)
        # col_num = len(grid[0])
        
        # counting the number of islands
        count = 0
        
        
        def dfs(i, j, grid):
            # Stop Depth first search when we reach boundary or water
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                # Using return to terminate recursion while using break to terminate loops
                return
            
            # To avoid repetive checking, we can choose to turn visited land/'1' to water/'0'
            grid[i][j] = '0'
            
            # If not encounter a boundary, let's check for all four sides
            
            dfs(i-1, j, grid)
            dfs(i+1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)
            
            
        for i in range(len(grid)):
            # Note: using grid[0] instead of grid[i] for loop increases the runtime by 10%
            for j in range(len(grid[0])):
                
                # We only check the surrounding when we got a land!
                # Update the count of an island after finishing ONE dfs searching
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    count += 1
        return count
                
        
            
           
                

                
                
            
            
                
