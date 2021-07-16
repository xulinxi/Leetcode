# 426. Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        
        
        # (Iterative) time: O(n); space: O(n) ----Cheney1993
        if not root: 
            return None
        
        stack = [root]
        
        # Initialize first and last for connection later
        first, curr, last = None, root.left, None
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue
                
            if stack: 
                curr = stack.pop()
                if not first:
                    first = curr
                    
                if last:
                    last.right = curr
                    curr.left = last
                
                last = curr
                curr = curr.right
                
        first.left = last
        last.right = first
        
        return first
