# 623. Add One Row to Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
       
        # Recursive Method------------------------------
        
        # (No helper function needed)
        
        # 1. base case:
        if root == None:
            return
        
        # If we has to insert the value into root, we create a new TreeNode and push the root down
        if d == 1:
            # Special case: recreate a new Treenode as a root
            return TreeNode(v, root, None)
        
        if d == 2:
            # This is the base case after the 1 (special case)
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
            
        else:
            # Recursive part: finding the d-1 level add the value in
            root.left = self.addOneRow(root.left, v, d - 1)
            root.right = self.addOneRow(root.right, v, d -1)
            
        return root
            
        
            
        
      # -----------Wrong answer------------ (recursive)  
        
        
        # We want to use the dfs to go to the givin depth
#         def dfs(node, current_depth, d-1, v):
            
#             if current_depth < d-1:
#                 dfs(node.left, current_depth+1)
#                 dfs(node.right, current_depth+1)
            
#             else:
#                 # When we reach the node with an level of d-1, we want to insert the node(s) with values of v beneath the node with the level of d (starting from the left)
#                 node.left = TreeNode
#                 node.left.val = v
#                 node.right = TreeNode
#                 node.left.val = v
                
                
                
            
#         dfs(root, 1, d-1, v)
        
#         return root





        
