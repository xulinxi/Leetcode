# 509. Fibonacci Number


class Solution:
    
    # Recursion-----------------------------
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             # Mistake 1:
#             # fib(n) = fib(n-1) + fib(n-2)
#             # return fib(n)
            
#             # Mistake 2:
#             # return fib(n-1) + fib(n-2)
            
#             return self.fib(n-1) + self.fib(n-2)


# # ------------------Top-Down Approach-------------
#         def fib(self, n: int) -> int:
#             if n <= 1:
#                 return n
            
#             # cache example:{n = 0: value = 0}
#             self.cache = {0:0, 1:1}
#             return self.memoize(n)
        
#         def memoize(self, n: int) -> {}:

#             if n in self.cache.keys():
#                 return self.cache[n]
            
#             self.cache[n] = self.memoize(n-1) + self.memoize(n-2)
#             return self.memoize(n)


# -----------------------Iterative Top-Down Approach
        def fib(self, n: int) -> int:
            if n <= 1:
                return n
            # if n == 2:
            #     return 1
            
            current = 0
            prev1 = 1
            prev2 = 0
            
            # Since range is exclusive and we want to include n, we need to put n+1
            for i in range(2, n+1):
                
                # *** 0 1 1 2 3 5 
                # current = the number we are calculating to proceed
                # for example, curr = 2; target n = 5
                # once we get current number, we update current to the next number while updating its previous two numbers as well
                
                current = prev1 + prev2
                prev2 = prev1
                prev1 = current 
            return current
            
            
            
            
            
            
        
