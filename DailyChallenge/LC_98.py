# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def checkBinaryTree(root, lower=float('-inf'), upper=float('inf')):
            if root:
                if root.val <= lower or root.val >= upper:
                    return False
                
                # Left subtree:
                if not checkBinaryTree(root.left, lower, root.val):
                    return False
                # Right subtree
                if not checkBinaryTree(root.right, root.val, upper):
                    return False
                    
                #     if root.left.val >= root.val:
                #         return False
                # if root.right:
                #     checkBinaryTree(root.right)
                #     if root.right.val <= root.val:
                #         return False
            return True
            
        return checkBinaryTree(root)
        
        
            
        
