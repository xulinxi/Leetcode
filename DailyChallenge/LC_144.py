# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
#         Iterative

        res_list = []
        stack_list = []
        
        while root!= None or len(stack_list) != 0:
            
            while root!= None:
                stack_list.append(root)
                res_list.append(root.val)
                root = root.left
            
            root = stack_list.pop()
            root = root.right
        
        return res_list
        
        
        
        
        
        # TODO: Recursive
        
        # return [root.val] + preorderTraversal(self, root)
        
