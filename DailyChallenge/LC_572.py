# 572. Subtree of Another Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Note: Similar to LC_100 - Same Tree
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        
        def isMatch(s, t):
            if not(s and t):
                return s is t
            return s.val == t.val and isMatch(s.left, t.left) and isMatch(s.right, t.right)
            
            
        if isMatch(s,t):
            return True
        if not s:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        
        
            
            
    
    
    
            
        
        
        
        
        
        
        
