# 62. Unique Paths

# Tutorial: https://www.youtube.com/watch?v=IlEsdxuD4lY

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # **** ex1: m = 3 (number of row); n = 7 (number of col)
        # Note: what we need: [numbers of nested list(3)]
        # [1]*n(number of units in a row) : size of each row
        dp = [[1]*n for i in range(m)]
        # print(dp)
        
        # for each row
        for x in range(1, m):
            # for each col
            for y in range(1, n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
   
                
        return dp[m-1][n-1]
        
        
        # --------------dp
        
#         # [1] * n: number of unit in col
#         # for _ in range(m) -> create ""[1] * n: number of unit in col" for m times
#         dp = [[1] * n for _ in range(m)]
#         # print(dp)
        
#         for col in range(1, m):
#             for row in range(1, n):
#                 # Traverse through each unit (except units in row 1 and col 1 since they all have 1 step for each), and calculate the step for each unit we traverse through
                
#                 dp[col][row] = dp[col-1][row] + dp[col][row-1]
                
#         return dp[m-1][n-1]
        
  
        
#         # ----------------------------Time Limit Exceeded

#         if m == 1 or n == 1:
#             return 1
#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
