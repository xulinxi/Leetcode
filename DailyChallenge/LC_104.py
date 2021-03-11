# 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
# Recursive Method----------------------------------------------------
        if root is None:
            return 0
        
        else:
            
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# (Wrong - No need to implement another helper function)
#         max_depth = 0
        
#         return self.dfs(root, 0)
        
#     def dfs(self, root, max_depth):
        
#         # Base case:
#         # 1. no more children -> max_depth += 0
#         # 2. find the max_depth of left and then find the max_depth of right -> compare them
        
#         left_max_depth, right_max_depth = 0, 0
        
#         if root:
#             max_depth += 1
                
#             left_max_depth = self.dfs(root.left, max_depth)
#             right_max_depth = self.dfs(root.right, max_depth)
            
#         return max(left_max_depth, right_max_depth)


# ---------------------------------------- #TODO Iterative
            
            
            
            
        
        
        
            
        
        
        
        
        
        
        
    
        
