class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        
        diff = []
        low, high = 0, 0
        
        for _, price in enumerate(map(float, prices)):
            c_diff = math.ceil(price) - price
            f_diff = price - math.floor(price)
            
            low += math.floor(price)
            high += math.ceil(price)
            
            # f_diff-c_diff: if > 0 , choose ceil; else: choose floor
            diff.append((f_diff-c_diff, f_diff, c_diff ))
            
            
        if not (low <= target <= high):
            return "-1"
        
        # ex: target = 8, low = 0+2+4 = 6; need 2 more numbers go through ceil operation
        ceil_N = target - low
        
        # sort the list in reversed order to make sure find the prices with min ceiling difference
        # ***Make sure sort the diff array NOT prices
        sorted_prices = sorted(diff, reverse=True)
        
        list_ceil = sorted_prices[:ceil_N]
        list_floor = sorted_prices[ceil_N:]
        
        sum_ceil = sum(d[2] for d in list_ceil)
        sum_floor = sum(d[1] for d in list_floor)
        
        res_sum = sum_ceil + sum_floor
        
        return "{:.3f}".format(res_sum)
        
        
        
        
        
        
        
        # ---------------------------------(greedy)
#         diff = []
#         low, high = 0, 0
        
#         # Note: map(fun, iter) -> map object with float value of each num in prices list; *** Get string values
#         for i, price in enumerate(map(float, prices)):
#             # Obtain floor value and ceiling value for each price
#             f_price, c_price = math.floor(price), math.ceil(price)
#             # low: stores min sum of all all prices; high: stores max sum
#             low, high = low + f_price, high + c_price
            
#             # Calculate the difference between current float or ceiling value with the current price
#             f_diff, c_diff = price - f_price, c_price - price
            
#             # Append a tuple with 3 values [ 1) the difference between f_diff & c_diff (if neg, we go with floor operation); if positive, f_diff > c_diff, go with ceiling; the greater d[0] is, the smaller c_diff is, 2) f_diff, 3)  c_diff ]
#             diff.append((f_diff - c_diff, f_diff, c_diff))
            
#         if not low <= target <= high:
#             return "-1"
        
#         # we need at least  ceil_n/N number (to ceil, aka + 1), with min value of 1, (target - low) to achieve target value
#         ceil_n = target - low
        
#         # Note: sorted(iterable, key=None, reverse=False)
#         # the greater d[0] is, the smaller c_diff is -> pick the first ceil_n within the reversed sorted list to choose the min c_diff to use

#         diff = sorted(diff, reverse = True)
        
#         # d: each diff_tuple in diff dictionary
#         # d[2]: (ceiling difference) c_diff for each price
#         # d[1]: (floor difference) f_diff for each price
        
# #         list1 = diff[:ceil_n] - first ceil_n should be ceil
# #         list2 = diff[ceil_n:] - after picking best prices with min c_diff, rest of prices should go with floor
            
#         ceil_prices = diff[:ceil_n]
#         floor_prices = diff[ceil_n:]

#         # Note: list comprehension:
#                 # This is just standard Python list comprehension. It's a different way of writing a longer for loop. You're looping over all the characters in your string and putting them in the list if the character is a digit.
#                 #   https://web.archive.org/web/20180309053826/http://www.secnetix.de/olli/Python/list_comprehensions.hawk
            
# #         sum1(ceil) = sum([d[2] for d in diff[:ceil_n]]) 
# #         sum2(floor) = sum([d[1] for d in diff[ceil_n:]])
        
#         sum_ceil_prices = sum(d[2] for d in ceil_prices)
#         sum_floor_prices = sum(d[1] for d in floor_prices)
        
#         res_sum = sum_ceil_prices + sum_floor_prices
#         return "{:.3f}".format(res_sum)
        
#         # The f then refers to "Floating point decimal format". The .3 indicates to round to 3 places after the decimal point.
# #         return "{:.3f}".format(sum([d[2] for d in diff[:ceil_n]]) + sum([d[1] for d in diff[ceil_n:]]))
            
            
            
        
