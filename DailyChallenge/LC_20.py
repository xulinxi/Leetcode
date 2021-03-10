# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        # Let's store each char of the giving string in to a stack
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            # Check 1. (check length) whenver you run out of stuffs to check (more close parentheses than open parenthesese)
            elif len(stack) == 0:
                return False
            
            # Check type (3 kinds)
            elif char == ')' and stack.pop() == '(':
                continue
                # continue: not check other if statements
                # pass: will check other if statements
            
            elif char == '}' and stack.pop() == '{':
                continue
                
            elif char == ']' and stack.pop() == '[':
                continue
                
            # Check 2: (if in order) If you don't have the open and close parentheses put in/written in string in order -> False
            else:
                return False
                
        # (check length) (more open parentheses than close parenthesese)
        return stack == []
            
        
        
