# 100. Same Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        
        
        # (DFS) time: O(n); space: O(n) ---- lxnn
        
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([(p.left, q.left), (p.right, q.right)])
                
            # if one of p or q is empty -> return false
            # BUG: else: return False
            elif p or q:
                return False
            
            # if both p and q is empty -> return True (defalt)
            
        return True
            
