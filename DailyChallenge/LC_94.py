# 94. Binary Tree Inorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
    # ***Note:
    #     - Iterative: Using Stack
    #     - Recursive: Using Recursion
        
# -------------------------INTERATIVELY--------------------------------------------------------
        result_list = []
        stack_list = []
        
        # As long as we still have items left in stack and the node(s) left to go through, 
        # we want to keep traversing through the tree
        while len(stack_list) != 0 or root != None:
            
            # we want to keep going to left until we reach the leftest node:
            #     - at the meantime: put the node that we passed through in stack (so we can pop them out when we reach their individual leftest node)
            
            #     - when there's no more left node, we get the value of the last left node (by popping the stack; last-in value is the value of current last left node (since the root is None, aka not-existing left node))
            #     - set the root = "leftest node"/current root.right
            #     - if there's a right node (aka root != null/None) -> we go through this process again (end of this big while loop)
            #     - if no right node: Pop the last value in the stack (aka the closest ancestor of that left tree; the "root" before the left tree becomes a root)
            #         - set its right node = root -> we go through this process again (end of this big while loop)
            # *** Note: we need to add the root to the stack, NOT just the value of the root! (when we pop the stack, we reset the root to it's previous ancestor)***
            
            # (walking through the tree): getting values in stack while searching through the left nodes
            while root != None:
                stack_list.append(root)
                root = root.left
            
            # if root == None (we reach out last left node); outside of the nested while loop
            root = stack_list.pop()
            result_list.append(root.val)
            root = root.right
            
        # if no more root left in the tree nor the stack: we finished! return out result_list!
        return result_list
      
      
      
      # TODO: RECURSIVE Method
    

            
            
            
                
                
                
                
                
                
                
                
                
                
                
        
