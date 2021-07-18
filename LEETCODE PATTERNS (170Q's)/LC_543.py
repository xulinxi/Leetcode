# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Correct Goal: find the longest path in the tree
        
        
        
        # (Iterative DFS) time: O(n); space: O(n) ---- jameskutw
        max_length = 0
    
        # since each left and right leaf will be added to 1, None will be -1
        depth = {None: -1}
        # if we only have 1 tree node -> 0 diameter
        stack = [(root, 0)]
        
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
                
            # 1st time visit, get its children (until the end)
            if visited == 0:
                stack.extend([(node, 1), (node.left, 0), (node.right, 0)])
            else:
                 # (Note: a leaf has a value of 0 (like when only one root in the tree; since None + 1 = 0))
                left_d = depth[node.left] + 1
                right_d = depth[node.right] + 1
                
                # (dp), update the max_diameter to each node:
                depth[node] = max(left_d, right_d)
                max_length = max(max_length, left_d + right_d)
        return max_length
        
        
        
        
        
        
        
        
        # (Wrong) ---- Mine
#         # BUG: Goal: find the max depth
#         max_depth = 0
        
#         if root:
#             stack = [(1, root)]
        
#         while stack:
#             depth, root = stack.pop()
#             children = [root.left, root.right]
            
#             # when reach a leaf -> check max_depth
#             if not any(children):
                
#                 # BUG: return max(max_depth, depth) -> will return the (first) max (we found the FIRST TIME)
#                 max_depth = max(max_depth, depth)
            
#             else:
#                 for c in children:
#                     # *** BUG: check if any children is NONE
#                     if c:
#                         stack.append((depth + 1, c))
                    
#         return max_depth
            
