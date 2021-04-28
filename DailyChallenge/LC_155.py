# 155. Min Stack

class MinStack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        
        # If the stack is empty, then the min value must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return
        
        # stack[x][1] is always the min number
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]







# -----------incorrect
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.minStack = []
#         self.min_element = float('inf')
#         self.sec_min = float('inf')

#     def push(self, val: int) -> None:
#         # print("push")
#         self.minStack.append(val)
#         if val < self.min_element:
#             if len(self.minStack) < 2:
#                 self.sec_min = self.min_element = val
#             else:
#                 self.sec_min = self.min_element
#                 self.min_element = val

#     def pop(self) -> None:
#         # print("pop")
#         x = self.minStack.pop()
#         if x == self.min_element:
#             self.min_element = self.sec_min

#     def top(self) -> int:
#         # print("top")
#         # print(self.minStack[-1])
#         return self.minStack[-1]

#     def getMin(self) -> int:
#         # print("getMin")
#         return self.min_element


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
