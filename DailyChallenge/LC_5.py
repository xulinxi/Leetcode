5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        if len(s) <= 1:
            return s
        
        res = ""
        def helper_check(s, l, r):
            # Make sure check range***
            while l>=0 and r< len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1 : r]
            
        for i in range(1, len(s)):
            odd = helper_check(s, i-1, i+1)
            even = helper_check(s, i-1, i)
            
            # Make sure remember your current longest palindromic substring
            if len(odd) > len(even):
                curr = odd
            else:
                curr = even
            
            res = curr if len(curr) > len(res) else res
                
                
        return res
            
            

        
        # -------------------------------------------------------

#         if len(s) <= 1:
#             return s
        
#         def check_palindrome(l, r):
#             while r < len(s) and l >= 0 and s[l] == s[r]:
#                 l-=1
#                 r+=1
#             return s[l+1:r]
        
#         ret = ''
        
#         for i in range(1, len(s)):
#             # if the palindrom has an odd length, i is the char in the middle, start checking the char around i
#             odd = check_palindrome(i-1, i+1)
#             # if even length: i is the right pointer
#             even = check_palindrome(i-1, i)
            
#             temp = odd if len(odd) > len(even) else even
#             ret = ret if len(ret) > len(temp) else temp
        
#         return ret  
        
        
        
        
        
        # -----------------------------
#         ans = ""
#         for i in range(len(s)):
            
#             # odd case
#             tmp = self.helper(s, i, i)
#             if len(tmp) > len(ans):
#                 ans = tmp
                
#             # even case
#             tmp = self.helper(s, i, i+1)
#             if len(tmp) > len(ans):
#                 ans = tmp
                
#         return ans
    
    
#     def helper(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
            
#         return s[l+1:r]

# --------------------------------------------

 
    
            
