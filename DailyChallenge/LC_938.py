# 938. Range Sum of BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 1. Compare high with root
        #     -> find the high (add to result)
        #     -> find all numbers (at the left branches of high) that numbers < high (add to result)
        # 2. Compare low with root
        #     -> find the low
        #     -> find numbers that are less than higher than low (right branches) that numbers > low
        
#         result = 0
        # Note: attribute 'root' does not exist, only its value exists in the class 'Solution'
        if root == None:
            return 0
        # if the low is greater than the root, no need to compare any branches at the left side -> move to right side
        if low > root.val:
            return self.rangeSumBST(root.right, low, high)
        # if the high is smaller than the root, no need to find any branches at the right side -> move to the left side
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)




        # -------------------------------------------------------------------------------
#             if root == None: return 0
            
#             if root.val < low: return self.rangeSumBST(root.right,low,high)
#             if root.val > high: return self.rangeSumBST(root.left,low,high)
            
#             return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)      
        
    # ----------------------------------------------------------------------------------------------------------
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         if root == None: return 0
#         if root.val > R: return self.rangeSumBST(root.left,L,R)
#         if root.val < L: return self.rangeSumBST(root.right,L,R)
#         return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)  
            
            
            
    
        
