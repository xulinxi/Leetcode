# 987. Vertical Order Traversal of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        # First, let's create a node_list to put all the nodes in here for future sorting
        node_list = []
        
        # Preorder search to get all nodes in a format of (root, row, col)
        def dfs(node, row , column):
            if node:
                node_list.append((column, row, node.val))
                
                # Once we append node, we call dfs recursively starting with
                # the left child and then the right child
                
                # Note: moving to the child, row + 1, to the left: col -1; to the right: col + 1
                dfs(node.left, row + 1, column - 1)
                dfs(node.right, row + 1, column + 1)
                
        dfs(root, 0, 0)
        node_list.sort()
        
        # Once we sort the list, we should have the node arrange from left to right
        # (from the smallest index to the largest index)
        
        # Let's create a result list
        res = []
        # Let's create an empty list for all values for current index.
        curr_col_val = []
        # Let's start with the smallest column number (from left to right)
        curr_col = node_list[0][0]
        
        for col, row, val in node_list:
            
            # If the current col if the one we are checking: we append its value to curr_col_val 
            if col == curr_col:
                curr_col_val.append(val)
                
            # If we've found all the value for certain index ->
            # (before we update the current checking col index) we need to:
            # - put all value in current index in result list
            # Then, we update the current checking col index
            # And we update the value for the current checking col index in curre_col_val
            
            else:
                res.append(curr_col_val)
                curr_col = col
                curr_col_val = [val]
                
        # Update the last append curr_col_val outside of the for loop 
        res.append(curr_col_val)
            
        return res
                
                
        
        
        
        
        
        
        
        
        
            
