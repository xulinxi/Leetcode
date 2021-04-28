# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        
        for token in tokens:
            # Check 1: if we encountered an operator, we pop two numbers from stack to operate on
            if token in ("+", "-", "*", '/'):
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    # Mistake 1: stack.append(num1 / num2) -> return a float number
                    # Mistake 2: stack.append(num1 // num2) -> 6/-132 = -1
                    # Note: we have to rount up to 0
                    stack.append(int(num1/num2))
            
            # Note: we need a else: statemnt here, so we don't append operator!!!
            else:
                # If we token != operator -> put the number in the stack
                # Mistake: stack.append(token) -> Make sure convert str to int
                stack.append(int(token))
            
        return stack.pop()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # --------Stack with lambda
        
#         operations = {
#             "+": lambda a, b: a + b,
#             "-": lambda a, b: a - b,
#             "/": lambda a, b: int(a / b),
#             "*": lambda a, b: a * b
#         }
        
#         stack = []
        
#         # Note: when we encountered an operation: we know that the operation will only operates on the two numbers before the encountered operation
#         for token in tokens:
#             if token in operations:
#                 number_2 = stack.pop()
#                 number_1 = stack.pop()
#                 # Make sure to stored the encountered operation
#                 operation = operations[token]
#                 # We append the final results after applying the operation on two numbers
#                 stack.append(operation(number_1, number_2))
                
#             else:
#                 stack.append(int(token))
#         return stack.pop()
        
        
