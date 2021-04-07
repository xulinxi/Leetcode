# 159. Longest Substring with At Most Two Distinct Characters

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        n = len(s)
        dictionary = {}
        max_len = 0
        start = 0
        
        for end in range(n):
            
            # dictionary still has enough space to take  (size <=2)

            dictionary[s[end]] = end
                               
            # Dictionary has no more space to take (size reach 3 (greateer than 2))  
            if len(dictionary) == 3:
                # Delete the leftmost character
                del_index = min(dictionary.values())
                del dictionary[s[del_index]]               
                               
                # Update start to the previous letter
                start = del_index + 1
                               
            max_len = max(max_len, end - start + 1)
                
        
        return max_len
