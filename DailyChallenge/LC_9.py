# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        len_x = len(str_x)
        l, r = 0, len_x -1
        
        for i in range(len_x):
            back_i = len_x - 1 - i
            if str_x[i] != str_x[back_i]:
                return False
        return True
