# 121. Best Time to Buy and Sell Stock
# Similar to 1. Two Sum
# Brute force is most obvious: find out the difference between numbers with their later numbers -> similar to Two Sum (but with a VERY large sample -> can't use brute force)
        
        # Brute force: exceede time limit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force is most obvious: find out the difference between numbers with their later numbers -> similar to Two Sum (but with a VERY large sample -> can't use brute force)
        
        # Brute force: exceede time limit
#         
#         for i in range(len(prices)-1):
#             difference = 0
#             if prices[i + 1] - prices[i] > 0:
#                 difference = prices[j + i + 1] - prices[i]
#                 if difference > peak:
#                     peak = difference
#         return peak
        # --------------------------------------------------
        min_price, max_profit = 100000, 0
    
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit
    
# --------------------------------------------------------------------------
        # max_profit, min_price = 0, float('inf')
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        # return max_profit
        
            

