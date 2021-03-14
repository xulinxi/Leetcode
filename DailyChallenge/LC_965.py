# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        
        left_correct = (root.left is None or root.left.val == root.val and self.isUnivalTree(root.left))

        right_correct = (root.right is None or root.right.val == root.val and self.isUnivalTree(root.right))
        
        
        # Another Mistake:-----------------------------------------------
        # We should check if root.left is None OR if left.val exists and the left branch is unival. Note: and has a higher priority than or
#         left_correct = (root.left.val == root.val or root.left is None and self.isUnivalTree(root.left))

#         right_correct = (root.right.val == root.val or root.right is None and self.isUnivalTree(root.right))
        
        return left_correct and right_correct
            
            
            
            # --------------_Wrong Recursion-------------------------
            # ***Note: we don't want to return this function because we only check the left side. Since we want to check both side of tree, we can store the left side result and right side result, then return them to see if both side is true.
            # # if root.left.val == root.val or root.left is None:
            # #     return self.isUnivalTree(root.left)
            # if root.right.val == root.val or root.right is None:
            #     return self.isUnivalTree(root.right)
            # else:
            #     return False
            
        # else:
        #     return True
        # -----------------------------------------------------------------------
        
        
        # -----------------TODO dfs-------------------------------------
            
