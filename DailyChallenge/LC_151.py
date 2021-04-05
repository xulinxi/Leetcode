# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(' ')
        s = s[::-1]
        s = ' '.join(s).strip()
        s = re.sub(' +', ' ', s)
        return s
        
       # ------------------------------- 
#         # Two pointers start from left end and right end:
#         left, right = 0, len(s) - 1
        
#         # Remove leading space
#         while left <= right and s[left] == ' ':
#             left += 1
#         # Remove trailing spce
#         while left <= right and s[right] == ' ':
#             right -= 1
            
#         # Reduce multiple spaces to single one
#         # Initialize output
#         output = []
        
#         while left <= right:
#             is s[left] != ' ':
#                 output.append(s[left])
#             elif output[-1] != ' ':
#                 left += 1
                
#             return output
    
#     def reverse(self, l: list, left: int, right: int) -> None:
#         while left < right:
#             l[left], l[right] = l[right], l[left]
#             left, right = left + 1, right -1
                
#     def reverse_each_word(l: list) -> None:
#         n = len(l)
#         start = end = 0
            
#         while start < n:
#               # Go to the end of the word
#             while end < n and l[end] != ' ':
#                 end += 1
#             # Reverse the word
#             reverse(l, start, end -1)
                
#             # Move tot he next word
#             start = end + 1
#             end += 1
        
#     def reverseWords(self, s: str) -> str:
#         # Convert string to char array
#         # and trim spaces at the same time
#         l = self.trim_spaces(s)
        
#         # Reverse the whole string
#         self.reverse(l, 0, len(l) - 1)
        
#         # Reverse the whole string
#         self. reverse_each_word(l)
        
#         return ''. join(l)
        
                
                
        
                
            
            
            
            
