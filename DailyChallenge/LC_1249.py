# 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        
    # Input: s = "lee(t(c)o)de)"
    # Output: "lee(t(c)o)de"  
    
    # Input: s = "a)b(c)d"
    # Output: "ab(c)d"
    
    # "t(8)"
    # 't(8'
    # 't)8'
    
#     # "a(b(c)d" "a(a(a("
#     stack = [] # numbers of items in the stack == numbers of "("
#     result = ""
#     # Iterate through the s (for loop)
#         # case1: (letter) append
#         # case2: ("(") -> append the curr letters/results that I accumulated
#         # case3: (")") -> (pop the stack if stack is not empty == inivible ")") -> "(" + result + ")"
#         #              -> (empty stack == extra ")") -> ignore extra ")" -> append rest of char
                
#         # if have extra "("  -> we'll have leftover items in stack (at the end of iteration) 
        
#         while item in stack:
#             result += item
            
#     return result

#     # time: O(n); space: O(n)

        # "(a(b(c)d)" out: a(b(c)d); (ab(c)d); (a(bc)d)
        
        # Initialize a stack and a result string
        stack = []    # ["", "a",    ]
        result = ""   # "b(c)d"
        
        # Iterate through input string
        for char in s:   # (,a, (, b, (, c, ), d, )
                                                  # | 
            # encounter "(" -> append curr result to stack
            if char == "(":
                stack.append(result) # result = ""  
                result = ""
                
            # encounter ")" -> if nothing in stack -> extend the result string with stack.pop() (get things out of stack)
                            # -> sth left in stack -> concatenate "(" + result + ")"
            elif char == ")":
                if stack:
                    result = stack.pop() + "(" + result + ")"  # "(b(c)d)"
                # Bug: else:
                #     result = stack.pop() + result
                    
            else:
                result += char   # result = "b(c)" + "d" = "b(c)d"  
                    
        # if we have extra "(" -> leftover in stacks after the iteration
        while stack: #a
            result = stack.pop() + result # a(b(c)d)
            
        return result
                    
            
                
            
        
        
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # (Stack and an empty string) ---- shuuchen
#         stack, cur = [], ''
        
#         for c in s:
#             if c == '(':
#                 stack.append(cur)
#                 cur = ''
#             elif c == ')':
#                 if stack:
#                     cur = stack.pop() + '(' + cur + ')' 
#             else:
#                 cur += c
        
#         # Since stack is recording down all substrings before '(' -> if we have extra "(" -> ignore extra "(" when we extend the result string
#         while stack:
#             cur = stack.pop() + cur
        
#         return cur
        
        
#         # a)b(c)d
#         # stack: ['ab',]
#         # cur: 'ab(c)d'
        
        
        
        
#         # Wrong (Stack and an empty string) ---- Mine
#         stack = []
#         result = ""
#         for char in s:
#             if char in "()":
#                 stack.append(char)
                
                
#         for char in s:
#             if char == "(" and ")" == stack.pop():
#                 result += char
#             # elif char == "(" and ")" != stack.pop():
#             #     continue
#             elif char == ")" and "(" == stack.pop():
#                 result += char
#             elif char not in "()":
#                 result += char
                
#         return result
            
                
            
