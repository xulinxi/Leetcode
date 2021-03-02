# 121. Best Time to Buy and Sell Stock
# Similar to 1. Two Sum

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force is most obvious: find out the difference between numbers with their later numbers -> similar to Two Sum
        
        peak = 0
        
        for i in range(len(prices)-1):
            for j in range(len(prices) - i - 1):
                difference = 0
                if prices[j + i + 1] - prices[i] > 0:
                    difference = prices[j + i + 1] - prices[i]
                    if difference > peak:
                        peak = difference
        return peak
        
