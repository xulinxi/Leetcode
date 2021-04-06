# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        # Get rid of any spaces
        sv = s.strip().split(' ')
        result = ''
        # print(sv)
        
        # We now loop through every char within the string after taking out spaces
        for i, e in enumerate(sv[0]):
            # We only add the char to the result string when it's a sign symbol(in the front) or a number
            if (i == 0 and sv[0][i] in ('-', '+')) or e.isnumeric():
                result += e
            else:
                break
                
        
        # 1. if all words, we broke and get here -> gotta catch the Value Error
        # 2. Check if integer falls within the value range
        try:          
            if int(result) <= -2 ** 31:
                return -2 ** 31
            elif int(result) >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return int(result)
        except ValueError:
            return 0
