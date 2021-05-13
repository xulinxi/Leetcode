# 322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            
            # we can start traverse at the value of current coin, 
            # becuase if current coin value is greater than the target value: 
            # -> we won't use this coin any way (use previous optimal coin solution)
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1

    
#     Why is the brute force not O(n!)?
    
#     (My proposed way:) -> (more like a top down method: starting with a target value)
#     ex: [1, 2, 5]
#         Start with 1: we have combinations of (1), (1, 2), (1,2,5) to make up **1** target values
#                    2: we have combinations of (2), (1,2,5) to make up 1 target values
#                    5: we have combinations of (5) to make up 1 target values
    
    # (Solution:) - brute force
    # Starting with a target value -> we have 3 coins (3 choices to choose from)
    # after we pick the 1st one, we then have according choices
    # .
    # .
    # .
    # the max will be: having coin 1: making 3 choices * the amount of target amount (number of times we need to make choices) => 3* 3*.... (the number of target amount) 
    
    
    

    
