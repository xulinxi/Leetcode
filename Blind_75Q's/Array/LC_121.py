class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # need 2 variables: curr_min and max_profit

        curr_min, max_profit = prices[0], 0

        for price in prices:
            if price < curr_min:
                curr_min = price
            if (price - curr_min) > max_profit:
                max_profit = price - curr_min

        return max_profit
