# 906. Super Palindromes

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        
        ans = 0
        l = int(left)
        r = int(right)
        
        # odd case
        # Step 1: The number we check must be a palindrome (doesn't has to be a super palindrome)
        for i in range(10**5):
            
            # Step 2: Check if the number is a palindrom
            s1 = str(i)
            # ex: s = 4321 in 123454321 palindrome
            s2 = s1[-2::-1]
            s = s1 + s2
            
            # Step 3: Squre the palidrome
            num = int(s) ** 2
            
            if num > r:
                break
                
            # Step 3: Check if the squred number results in a palidrome that falls within the range
            if num >= l and str(num) == str(num)[::-1]:
                ans += 1
                
        # even case
        for i in range(10**5):
            s1 = str(i)
            # ex: s = 4321 in 123454321 palindrome
            s2 = s1[::-1]
            s = s1 + s2
            num = int(s) ** 2
            if num > r:
                break
            
            if num >= l and str(num) == str(num)[::-1]:
                ans += 1    
        
        return ans
