# 700. Search in a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        
        elif root.val < val:
            # ***Note: use self.!!!!
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        
        
        # ----------------------_Wrong answer (Binary)-------------------
#         def dfs(root):
#             if root:
#                 if root.val == val:

#                     return root

#                 dfs(root.left)
#                 dfs(root.right)

#             return None
        
#         # Base case: only root exists:
#         if root:
#             dfs(root)

#         return dfs(root)
        

        
            
        
                
                
        
