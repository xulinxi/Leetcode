# 139. Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # ------Brute Force (recursion and backtracking) ----O(2^n) exceed time limit
#         def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            
#             # After check the last valid string -> finish looping -> return True
#             if start == len(s):
#                 return True
                
#             # check all letter combination within the string (in order)
#             # Make sure to check all word combinations starting from the second index (more like two for loops traversing through the string)
#             for end in range(start + 1, len(s) + 1):
                
#                 # wordBreakRecur(s, word_dict, end) checks if there's any segment after the end (we sliced the first segment) -> this happends when s[start:end] in word_dict is true
#                 if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
#                     return True
#             return False
        

#         # set can be used to decrease the runtime complexity
#         return wordBreakRecur(s, set(wordDict), 0)



# --------------Approach 2: Recursion with memoization ----
        

# ---------Approach 3: Using Breadth-First-Search --------
#         # Initialize word_set, queue for storing the next word's first index, and the index for the words we visited
#         word_set = set(wordDict)
#         queue = deque()
#         visited = set()
        
#         # start with the first index in queue
#         queue.append(0)
#         # As long as the q is not empty, we have char(s) to check
#         while queue:
#             start = queue.popleft() 
#         # If we've checked this index for any viable word, we move forward
#             if start in visited:
#                 continue
#         # We extend the end index for the word
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in word_set:
#                     # Append the next index to the queue, if we can find this word in the word_set
#                     queue.append(end)
                    
                
#                 # Make sure to reurn True after we check the last viable word 
#                     if end == len(s):
#                         return True
                    
#                 # Make sure to store the visited first index for viable word
#                 visited.add(start)
        
        
#         # Return False if there's a visited start in visited set
        
#         return False

 # ---------------Dynamic Programming ----------------
    

        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]









