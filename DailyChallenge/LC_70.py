# 70. Climbing Stairs



class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # Note: climb 1 or 2 steps can be counted as the same "one last step"
        # -> Therefore, the different ways to climb at the current stair will be the different ways of stair(n-1) or stair(n-2)
      
    
    
    # --------- DP / Fibonacci
        if n == 1:
            return 1
        
        # Note: 0 is included, so the list size should be n+1
        # Mistake: dp = [None] * n 
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        print(dp)

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        # dp[3] = dp[1] + dp[2]
        
        return dp[n]
    
    
    
    
    
    
    
    
    
    # ------------------Time Limit Exceeded
#         if n <= 3:
#             return n
        
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
