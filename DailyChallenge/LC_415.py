# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Two methods off top of my head:
            # 1. convert two nums into integers using ord first, and then do the math
            # 2. Using linked list method: using a carry
            
        res_list = []
        res = ""
        carry = 0
        index_1 = len(num1) - 1
        index_2 = len(num2) - 1
        
        # while index_1 > 0 and index_2 > 0:
        while index_1 >= 0 or index_2 >= 0:
            # Mistake: should set the value to 0 if one of the string is running out of number
            # curr_1 = ord(num1[index_1]) - ord('0')
            # curr_2 = ord(num2[index_2]) - ord('0')
            # curr_1 = ord(num1[index_1]) - ord('0') if index_1 > 0 else 0
            curr_1 = ord(num1[index_1]) - ord('0') if index_1 >= 0 else 0
            curr_2 = ord(num2[index_2]) - ord('0') if index_2 >= 0 else 0
            
            
            # Mistake: curr_sum, carry = divmod(curr_1 + curr_2 + carry, 10)
            carry, curr_sum = divmod(curr_1 + curr_2 + carry, 10)
            res_list.append(curr_sum)
            index_1 -= 1
            index_2 -= 1
        
        if carry:
            res_list.append(carry)
            
        for num in res_list[::-1]:
            res = res + str(num)
            
        return res
            
        
        
