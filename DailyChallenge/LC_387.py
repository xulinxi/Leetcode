# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
                
        # ****
        for inx in range(len(s)):
            if dict_s[s[inx]] == 1:
                return inx
        
        return -1
                
        
