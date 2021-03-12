# 110. Balanced Binary Tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # check the two big left sub and right sub tree, check each small sub left and sub right trees
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

    def height(self, root: TreeNode):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
        
        
        # ---------------------------------Wrong recursive method (need a separate function: main function: return boolean; helper: return height (int))
#         if root is None:
#             return True
        
#         else:
#             leftDepth =  1 + self.isBalanced(root.left)
#             # print("left", leftDepth)
#             rightDepth =  1 + self.isBalanced(root.right)
#             # print("right",rightDepth)
            
#             return abs(leftDepth - rightDepth) < 1:
#                 return False


# -------------------------------------------------------------
# Iterative Method
    

        
