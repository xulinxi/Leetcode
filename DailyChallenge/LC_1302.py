# 1302. Deepest Leaves Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
#         # Recursion:

#         # Since we need to find the depth first and then find the sum of each deepest leaf,
#         # these two variables can be updated within a helper function.
#         max_depth = 0
        
#         sumM = 0
        
#         def dfs_sum(root, level):
#             # Make sure to label the variable within the helper function as non local
            
#             nonlocal max_depth 
#             nonlocal sumM 
           
#             if root:
#                 if level > max_depth:
#                     max_depth = level
#                     sumM = root.val

#                 # Must be "elif" statement because after the previous if statement, next one will always pass
#                 elif  level == max_depth:
#                     sumM = sumM + root.val
                
#                 dfs_sum(root.left, level + 1)
#                 dfs_sum(root.right, level + 1)
                
#             else:
#                 return 
            
#         dfs_sum(root, 0)
#         return sumM
  
    
    # ----------_Referenced Solution - Recursion-----------
#         depth = 0
#         total = 0
        
#         def treeSum(root, curdepth):
#             nonlocal depth
#             nonlocal total
#             if root is None:
#                 return
#             if curdepth > depth:
#                 depth = curdepth
#                 total = root.val
#             elif curdepth == depth:
#                 total += root.val
#             treeSum(root.left, curdepth+1)
#             treeSum(root.right, curdepth+1)
            
        
#         treeSum(root, 0)
#         return total


        # Iterative - Preorder - DFS Method:---------------------

        stack = [(root, 0) ]
        sum_depth, depth = 0, 0
        
        # Use while loop to check and to stop whenever we are running out of items in the stack (not a if statement!)
        while stack:
            node, level = stack.pop()
            if node: 
                if node.left == None and node.right == None: # We reach a leaf -> Let's check if this has the deepest depth
                    if level > depth:
                        # If current level is greater, let's update the depth with the value of the new depth
                        # & clear out the previous sum for depth
                        sum_depth = node.val
                        depth = level

                    # "elif" statement should be used since in the previous if statement we set depth = level   
                    elif level == depth:
                        # If current level is the same as the depth, add the current node.val to sum_depth
                        sum_depth += node.val

                # If we haven't reach the leaf, let's keep appending the children into the stack using the order of: right -> left -> node
                else:
                    # Make sure to append a tuple with (node, current depth/level + 1) to go to the node in the next level
                    stack.append((node.right, level + 1))
                    stack.append((node.left, level + 1))

     # ***At the end, we want to return the answer
        return sum_depth
    
    
    
    
            
                



             
        
            
                
        
            
            
    
        
        
