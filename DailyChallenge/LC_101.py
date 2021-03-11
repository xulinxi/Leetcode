# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # Iterative Method--------------------------------------------------------
        
        
        # (BFS)-------------------------------------------
        queue = []
        
        queue.append(root)
        queue.append(root)
        
        while queue:
            leftSub = queue.pop(0)
            rightSub = queue.pop(0)
            
            if leftSub is None and rightSub is None:
                # !!!Note: in iterative we have to continue checking, but in recursive we can return true becuase we've reached the base case!!!
                continue
            if leftSub is None or rightSub is None:
                return False
            if leftSub.val != rightSub.val:
                return False
            
            # If leftSub == RightSub:
            queue.append(leftSub.left)
            queue.append(rightSub.right)
            queue.append(leftSub.right)
            queue.append(rightSub.left)
            
        # If every goes through at the end -> finish checking every node -> mirror tree
        return True
            
                
                

        
        
#         # Recursive Method--------------------------------------------------
#         if root:
#             # if want to refer isMirror before implement it, we need to put self. before the method name
#             return self.isMirror(root.left, root.right)
#         else:
#             return True
            
#     def isMirror(self, left, right):
        
#         # List out two base cases: 1. empty 2. non-empty
        
#         # 1. empty: left and right both empty or just one side is empty
#         # Note: no need to compare their values, just to check if they exist.
#         if left is None and right is None:
#             return True
#         if left is None or right is None:
#             return False
        
#         # 2. non-empty
#         if left.val == right.val:
#             # check outer left and outer right, inner left and inner right
#             checkOuter = self.isMirror(left.left, right.right)
#             checkInner = self.isMirror(left.right, right.left)
#             return checkOuter and checkInner
#         else:
#             return False

        # ----------------------------(referenced answer)
#       def isSymmetric(self, root):
#         if root is None:
#           return True
#         else:
#           return self.isMirror(root.left, root.right)

#       def isMirror(self, left, right):
#         if left is None and right is None:
#           return True
#         if left is None or right is None:
#           return False

#         if left.val == right.val:
#           outPair = self.isMirror(left.left, right.right)
#           inPiar = self.isMirror(left.right, right.left)
#           return outPair and inPiar
#         else:
#           return False
        
        
