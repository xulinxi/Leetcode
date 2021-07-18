# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        
        
        # (DFS Iteration) time: O(n); space: O(n) ---- Solution
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            
            # if children == None -> update min depth
            if not any(children):
                # print(children, any(children))
                min_depth = min(depth, min_depth)
                
            # if children -> append each child into the stack
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth 
        
        
        
        
        
          # (DFS Iteration) time: O(n); space: O(n) ---- Mine
#         # Depth First Search
        
#         min_depth = 0
#         stack = [(1, root)]  # 9, 20
         
#         while stack:
#             curr_depth, root = stack.pop() # curr_depth, root = 1, 3
#             min_dep
#             stack.extend((curr_depth + 1 if root.left else curr_depth, root.left), (curr_depth + 1 if root.left else curr_depth, root.right))
#             while stack
            
            
        
