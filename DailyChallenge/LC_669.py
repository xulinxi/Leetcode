# 669. Trim a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        if root:
            # 3 base cases:
                # 1. root node is less than the low 
                # 2. root node is greater than the high 
                # 3. root node is between the low and high -> valid

            # 1st case: Root node is less than the low -> trim the left side of the tree/root (trim all the left subtree, *** including the node) (ignore/trim the left subtree)
            if root.val < low:
                return self.trimBST(root.right, low, high)

            # 2nd case: Root node is greater than the high -> trim the right side of the tree/root (trim all the right subtree, *** including the node) (ignore/trim the right subtree)

            if root.val > high:
                return self.trimBST(root.left, low, high)

            # 3rd case: Current root value is wihin the range:

            else:
                # In this problem, we are **changing the tree**, so we have to keep reassigning the left and right subtrees
                root.left = self.trimBST(root.left, low, high)
                root.right = self.trimBST(root.right, low, high)
                
        return root

        
        
        
        
        
#         if root is None:
#             return root
        
#         else:
            
#             # Base cases: 1. fall within the range -> keep it 2. don't fall within the range -> remove it
                
#             if low <= root.val <= high:
#                 continue
                
#             else:
#                 # Reassigning the left and right of a node
                
            
        
