# 404. Sum of Left Leaves


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # ------------------Recursive method------------------------------------
        
        left_sum = 0
        
        if not root:
            return 0
    
        # A helper function to traverse through the tree using dfs - preorder
        def dfs(root):
            
            nonlocal left_sum
            if root:
                # if a LEFT leaf:
                if root.left and root.left.left is None and root.left.right is None:
                    left_sum += root.left.val
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
                
            return left_sum
        
        dfs(root)
        
        return left_sum
    
    
    
    
    # ----------------------------Iterative method-----------------------------------------
    
    
        
        
        
        
