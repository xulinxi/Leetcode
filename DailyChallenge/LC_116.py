# 116. Populating Next Right Pointers in Each Node


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
         
        
        if not root:
            return None
        
        # Starting with left, if left.next exits we connect children on the same level
        if root.left:
            root.left.next = root.right
            
            # link the left's right child to the right's left child
            # ***Make sure to check if root.next follwing statement WITHIN the root.left
            if root.next:
                root.right.next = root.next.left

        # ***Make sure use self. and return statement at the end!
        self.connect(root.left)
        self.connect(root.right)
        
        return root
        
            
