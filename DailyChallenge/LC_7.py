# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:

#         negFlag = 1
#         if x < 0:
#             negFlag = -1
#             strx = str(x)[1:]
#         else:
#             strx = str(x)

#         x = int(strx[::-1])
        
#         return 0 if x > pow(2, 31) else x * negFlag
    
    
#     ----------------------(wrong->correct)-----------
        if abs(x) < 10:
            return x
        
        reverse = ""
        str_int = str(x)
        len_int = len(str_int)
        start = 0
        if str_int[start] in ("-", "+"):
            reverse += str_int[start]
            start += 1
        for i in range(len_int-1, start-1, -1):

            # index = len_int - i - 1
            reverse += str_int[i]
            
        return int(reverse) if int(reverse) <= pow(2, 31) and int(reverse) >= pow(-2, 31) else 0
    
    
#     --------------------
#             result = 0

#         if x < 0:
#             symbol = -1
#             x = -x
#         else:
#             symbol = 1

#         while x:
#             result = result * 10 + x % 10
#             x /= 10

#         return 0 if result > pow(2, 31) else result * symbol
