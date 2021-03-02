# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        
#         # The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )
#         # Note: no need to reset the count_left and count_right since the brackets before 1 are also the brackets before 2!!!
        
        max_count = 0
        
        count = 0
        

        for char in s:

            if char == "(":
                count += 1
                # print(char, count_left)
            # elif doesn't work; if elif is true, else statement cannot get updated without a non-")"/"(" char; the else statement will happen if the second if statement is not happen (ignore first if statement)
            if char == ")":
                count -= 1
                # print(char, count_right)
            
            else:
                # print(char)
                # print(count_right, count_left, pair)
                if count > max_count:
                    max_count = count
                # print(pair, max)

        return max_count


            
        
