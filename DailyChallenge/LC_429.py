# 429. N-ary Tree Level Order Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # Often, recursion cannot be used in Breadth-first Search
#         To do a breadth-first search, we use a queue.
#         That is because breadth-first search is based on using a queue, whereas recursion is using the runtime stack and so is suited to depth-first search. 

        # Note: Using pop(0) to emulate dequeue when we are implementing queue using a list
        
        if root is None:
            return []
        
        result = []
        previous_level = [root]
        # previous_level.append(root)
        print(previous_level)
        
        while previous_level:
            current_level = []
            result.append([])
            for node in previous_level:
                result[-1].append(node.val)
                current_level.extend(node.children)
            previous_level = current_level
        return result
    
    



# -------------solution
#         if root is None:
#             return []        

#         result = []
#         previous_layer = [root]

#         while previous_layer:
#             current_layer = []
#             result.append([])
#             for node in previous_layer:
#                 result[-1].append(node.val)
#                 current_layer.extend(node.children)
#             previous_layer = current_layer
#         return result
            
            
