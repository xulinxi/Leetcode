# 637. Average of Levels in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        
        
        
        
        
        
        
        # (Breadth First Search) time: O(n); space: O(m); m = max number of nodes at any level in the in put tree ---- Solution/DBabichev
        # breadth first search (use a helper function) -> use queues
        result = []
        # Storing the nodes of current level
        queue = deque([root])
        
        while queue:
            # Storing the values of current level (from popping the node values from queue)
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))
            
        return result
        
        
