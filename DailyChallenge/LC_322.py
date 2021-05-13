# 322. Coin Change

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
        
#         for coin in coins:
            
#             # we can start traverse at the value of current coin, 
#             # becuase if current coin value is greater than the target value: 
#             # -> we won't use this coin any way (use previous optimal coin solution)
#             for x in range(coin, amount + 1):
#                 dp[x] = min(dp[x], dp[x - coin] + 1)
                
#         return dp[amount] if dp[amount] != float('inf') else -1

    
