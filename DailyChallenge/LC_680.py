# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # print(left, right, s[left, right-1], s[left+1, right])
                # print(left, right)
                # print(s[left, right-1], s[left+1, right])
                return self.checkPalindrome(s, left, right - 1) or self.checkPalindrome(s, left + 1, right)
            else:
                left += 1
                right -= 1
        return True
        
        
        
        
    def checkPalindrome(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            
            
            # (Two Pointers) ---- GraceMent
#     def validPalindrome(self, s):
#         i, j = 0, len(s) - 1
        
#         while i < j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
#         return True
    
#     def validPalindromeUtil(self, s, i, j):
#         while i < j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return False
        
#         return True
        
        
        
        # (Wrong) ---- Mine
#         # count = 0
        
#         low, high = 0, len(s) - 1
        
#         while low < high:
#             if s[low] != s[high]:
#                 # print(s[low:high], s[high-1:low+1:-1], s[low+1:high+1], s[high:low+2:-1])
#                 # print(s[low:high])
#                 # print(s[high-1:low:-1])
#                 print(s[low:high], s[high-1:low:-1], s[low+1:high+1], s[high+1:low+1:-1])
#                 return s[low:high] == s[high:low:-1] or s[low+1:high+1] == s[high+1:low+1:-1]
                
#             # elif count > 1:
#             #     return false
#             low += 1
#             high -= 1
#         return True
            
                
