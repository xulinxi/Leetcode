# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        
        L, n = len(needle), len(haystack)
        
        if L == 0:
            return 0
        
        pn = 0 # Pointer on the haystack
        while pn < L - n + 1:
            # Find the position of the first needle character
            # in the haystack string
            while pn <  n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
                
            # Computer the max match string
            curr_len = pL = 0 # curr_len of the needle we are at
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1
                
            # If the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L
            # Otherwise, backtrack-> update pn to the next pn
            pn = pn - curr_len + 1 
            
        return -1
        
