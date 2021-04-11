124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # max sum on the left and right sub-trees of node (when staying on current "root" node)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # the price to start a new path where 'node' is a highest node
            # sum of (left-> node->right)
            price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
            # Node: if left and right both were calculated and the sum was updated a new path was created becase we can only pass the current "root" node once
            max_sum = max(max_sum, price_newpath)
            
            # for recursion:
            # return the max gain if continue the same path
            # Since staying on the current "root" node, only the (one of the) child with the max val will be added
            return node.val + max(left_gain, right_gain)
        
        max_sum = float("-inf")
        max_gain(root)
        return max_sum
        
        
        
        
        
