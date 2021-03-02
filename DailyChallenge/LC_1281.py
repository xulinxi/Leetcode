# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        # Convert the number to a string, separate out each digits then to the manipulation
        # Using module is also a way to solve it
        
        n_str = str(n)
        sum_of_dig = 0
        product_of_dig = 1
        
        for digit in n_str:
            sum_of_dig += int(digit)
            product_of_dig *= int(digit)
            # print(sum_of_dig, product_of_dig)
            
        return product_of_dig - sum_of_dig 
