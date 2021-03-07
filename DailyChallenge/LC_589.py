"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # Recursive Method----------------------------------------------
        
#         result = []
        
#         def dfs(root):
#             if root:
#                 result.append(root.val)
#                 for child in root.children:
#                     dfs(child)
#         dfs(root)
        
#         return result

        # Iterative Method--------------------------------------------------
    
        result = []
        stack = []
        stack.append(root)
        # print(root.val, queue)
    
        while stack:
            if root:
                root = stack.pop()
                result.append(root.val)
                # print(root.children[::-1])
                stack.extend(root.children[::-1])
            else:
                return result
        
        return result

    # Resource: https://www.youtube.com/watch?v=HOMjIiztImo
                    
                
            
                
                    
                        
            
            
            
            
            
            
            
        
        
