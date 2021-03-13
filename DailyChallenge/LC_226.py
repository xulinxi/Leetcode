# 226. Invert Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
  
        # ---------------------------Recursive Method-------------------
        if not root:
            return root
        
        else:
            
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left

            # (confusing answer; try understand it?)
            # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            
        return root
    
    
    
    # --------------------#TODO Iterative-------------------------------------
            
