# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     
        max_len = 0
        len_s = len(s)
        prev_chars = {}
        # print(len(s))
        # print(len(s) - 1)
        
        start = 0
        for end in range(len_s):
            # curr_len = 0
            # if s[end] not in prev_chars:
            #     prev_chars[s[end]] = 1
            #     curr_len = end - start + 1
                
            if s[end] in prev_chars:
                # s[end] is the index of current end
                # prev_chars[s[end]] gets the max index where the duplicate appear
                start = max(prev_chars[s[end]], start)

                
            max_len = max(max_len, end - start + 1)
            prev_chars[s[end]] = end + 1
            
        return max_len

            
            
