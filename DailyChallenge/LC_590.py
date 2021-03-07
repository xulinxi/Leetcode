# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        
        # Recursive Method:-----------------------------------
#         result = []
        
#         def dfs(root):
#             if root:
#                 for child in root.children:
#                     dfs(child)
#                 result.append(root.val)
#         dfs(root)
#         return result


        # Iterative Method:------------------------------------------
        stack = [root,]
        result = []
        
        while stack:
            if root:
                root = stack.pop()
                result.insert(0, root.val)
                stack.extend(root.children)
                # root = stack.pop()
            else:
                return result
        return result
    
    # Resource: https://www.youtube.com/watch?v=Ds5e1A88j7Q
            


                    
                    
            
                
            
                
                
                
        
        


                
        
        
