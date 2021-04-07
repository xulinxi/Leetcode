# 186. Reverse Words in a String II

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse_words_helper(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        reverse_words_helper(0, len(s)-1)
        
        left = 0
        
        for index, char in enumerate(s):
            if char == " ":
                reverse_words_helper(left, index-1)
                left = index + 1
                
        reverse_words_helper(left, len(s)-1)
            
        
