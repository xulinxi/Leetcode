class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [len(temperatures) - 1]
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)   
    
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # 1. initialize stack and res array
#         stack = []
#         res = [0] * len(temperatures)
        
#         # 2. For each element temperatures[i] backwards
#         #     - pop until stack is empty or top of stack > temperatures[i]
#         for i in range(len(temperatures) - 1, -1, -1):
#             while stack and temperatures[i]  >= temperatures[stack[-1]]:
#                 stack.pop()
        
#             if not stack: # if there's no temp that is greater than curr temp
#                 res[i] = 0
#             else: # there's at least 1 temp that is greater than curr temp
#             # 3. Calculate distance from temperatures[i] to top of stack
#                 res[i] = stack[-1] - i

#             stack.append(i)
        
#         return res
                
            
        
        
        
            

            
        
        
        
        
        
        
        
        
