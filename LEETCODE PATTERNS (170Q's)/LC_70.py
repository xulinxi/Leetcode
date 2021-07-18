# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # (Dynamic Programming) time: O(n); space: O(1) ---- Solution
        
        # Note/Mistake: this edge/base case should be individually returned
        if n == 1:
            return 1
        
        # Note/Mistake: if index of the dp array will be needed to generate/accumulate subsolution, we have to initialize the dp array with a fixed size at the start.
        
        dp = [0] * (n+1)
        print(dp, n)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
        
        
        
        
#         # (Recursion with Memoization) time: O(n); space: O(n) ---- Solution
#         # Note: this function must be declared before calling it
#         def climb_Stairs(i, n, memo):
#             if i > n:
#                 return 0
#             if i == n:
#                 return 1
#             if memo[i] > 1:
#                 return memo[i]
            
#             memo[i] = climb_Stairs(i+1, n, memo) + climb_Stairs(i+2, n, memo)
#             return memo[i]
        
#         # (Recursion with Memoization)
#         memo = [0] * (n+1)
#         return climb_Stairs(0, n, memo)
        
        
        
#         # (Fibonacci Number - For loop) time: O(n); space: O(1) ---- Solution
#         if n == 1:
#             return 1
    
#         first = 1
#         second = 2
        
#         for i in range(3, n + 1, 1):
#             third = first + second
#             first = second
#             second = third
            
#         return second
        
        
        
        
        
        
        
        # (Fibonacci Number Recursion) Time Limit Exceeded; time: O(n); space: O(1) ---- Mine
#         if n == 1:
#             return 1
        
#         # Note/Mistake: n == 2 is also one of the base case since there is 
#         # no climbStairs(n-2) available.
#         elif n == 2:
#             return 2
        
#         else:
#             return self.climbStairs(n-2) + self.climbStairs(n-1)
