# 222. Count Complete Tree Nodes



# Note: In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes at the last level h. An alternative definition is a perfect tree whose rightmost leaves (perhaps all) have been removed. Some authors use the term complete to refer instead to a perfect binary tree as defined below, in which case they call this type of tree (with a possibly not filled last level) an almost complete binary tree or nearly complete binary tree. A complete binary tree can be efficiently represented using an array.

# A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.

# A complete binary tree is just like a full binary tree, but with two major differences

# All the leaf elements must lean towards the left.
# The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
       
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0
    
    
    # -------------------(Wrong)
#         count = 0
        
#         def count_node(root, count):
#             if root:
#                 count += 1
                
#                 left = count_node(root.left, count)
#                 right = count_node(root.right, count)
#                 total = left + right
                
#                 return count
        
#         count_node(root, count)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
