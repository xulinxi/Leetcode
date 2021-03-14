# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
# --------------------Recursive method--------------------------------
        # Base case 1: empty tree
        if not root:
            return 0

        # Base case 2: leaf/single node
        if not root.left:
            return self.minDepth(root.right) + 1
        # return to avoid elif statement
        elif not root.right:
            return self.minDepth(root.left) + 1
        
        # Recursive Case
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        
        
        
        
        
        # ---------------------------- Iterative-----------------------------
        
        
        
        
        
        
        
            
        
        
                
                
        
