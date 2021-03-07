# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
#         res = []
#         stack_list = []

        
#         while root or stack_list:
#             while root:
#                 if root.right:
#                     stack_list.append(root.right)
#                 stack_list.append(root)
#                 # Keep looping until we go the leftmost leaf
#                 root = root.left
            
#             # Root should be pop to get its root.right value
#             root = stack_list.pop()
                
#             # Check if right tree has been proceed
#             if stack_list and stack_list[-1] == root.right:
#                 # put the root back to the list for later check
#                 stack_list[-1] = root
#                 # Set right node of the root as the root to check if there's any more children
#                 root = root.right
                
#             else:
#                 # No more right node (and no more left node) -> get the value and reset node,
#                 # so new root can be set by popping the next node that's available in the stack
#                 res.append(root.val)
#                 root = None

    
#         return res
    
    
    
    # ----------------------------------------------------(Solution_iterative)

#         stack, output = [], []
#         while root or stack:
#             # push nodes: right -> node -> left 
#             while root:
#                 if root.right:
#                     stack.append(root.right)
#                 stack.append(root)
#                 root = root.left
            
#             root = stack.pop()
            
#             # if the right subtree is not yet processed
#             if stack and root.right == stack[-1]:
#                 stack[-1] = root
#                 root = root.right
#             # if we're on the leftmost leaf
#             else:
#                 output.append(root.val)
#                 root = None
                
#         return output
    
    
    # -----------------------------------------------------------------
    
    # TODO: Recursive
        
        res_list = []
        
        # Create a helper function to iterate via the tree, then call the helper function
        def dfs(root):
            if root:
                
                dfs(root.left)
                dfs(root.right)
                
                # Just change the position when you append the root value
                res_list.append(root.val)
                
        dfs(root)        
                
        return res_list
                
                
            
            
