# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Goal: Find a min value in the array AND we find the number (after the min) that has greatest positive difference -> to make the max profit
        
        # min_val = prices[0]  *** 1
        # max_profit = 0        *** 6
        
        # Iterate through the prices array:
        #     case 1 : next number < min num -> update min *** min_val = 1
        #     case 2 : next number > min num -> calculate the profit -> compare curr profit with max profit
        #         case 2.1: if curr profit > max profit -> reset the max profit *** max_profit = 6
        #         case 2.2: if not: keep max profit
        #       
        
        # At the end (of array) -> retur max profit = 6
        
        # time: (1 for loop) O(n); space: O(1)
        
        # [7,2,8,1,6,4] output: 6 
        
        # Noted: - have (general) thought process down first, then use an example to explain it.
            
            
        # Initialize min_val and max_profit
        min_val, max_profit = prices[0], 0
        
        # Iterating through the prices array (updating min_val and max_profit)
        
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                
            elif (prices[i] - min_val) > max_profit:
                max_profit = prices[i] - min_val
                
        return max_profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # （One Pass）time: O(n); space: O(1) ---- Solution
        
        # Step 1: since there's the low and high in the stock market: initialize min_price and max_profit
#         min_price = float("inf")
#         max_profit = 0
        
#         for i in range(len(prices)):
#             # since we are going from left to right -> we are finding the min in "later days"
#             if prices[i] < min_price:
#                 min_price = prices[i]
        
#             # if current price is greater than min_price -> indicates we can make a profit -> check if it's greater than the current max_profit
#             elif prices[i] - min_price > max_profit:
#                 max_profit = prices[i] - min_price
                
#         return max_profit
