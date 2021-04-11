# 109. Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # (Inorder Simulation)---------------------
    def findSize(self, head): # Time: O(n)
        pointer = head
        # c records the len(head/linkedlist)
        c = 0
        while pointer:
            pointer = pointer.next
            c += 1
        return c
    
    def sortedListToBST(self, head):
        
        # Get the size of the linked list first
        size = self.findSize(head)
        
        # Recursively form a BST out of linked list from 1 --> r
        def convert(l, r):
            nonlocal head
            
            # Invalid case
            if l > r:
                return None
            
            mid = (l + r) // 2
            
            # First step of simulated inorder traversal.
            # Recursively form the left half
            left = convert(l, mid - 1)
            
            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left
            
            # Maintain the invariance mentioned in the algorithm
            head = head.next
            
            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)
            
            
            
    
    
    
    
    
    
    
    # ----------------Recursion (linked list and helper function to find the mid node)
#     def findMiddle(self, head):
        
#         # The pointers used to disconenct the left half from the mid node.
#         prev = None
#         slow = head
#         fast = head
        
#         # Iterate until fast pointer doesn't reach the end end of the linked list.
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             # fast pointer move slow_step * 2
#             fast = fast.next.next
            
#         # Handling the case when slow pointer was equal to head.
#         # Prev stops at one node before where slow (mid) stops
#         # To disconnecting, the left portion, we set prev.next = None
#         if prev:
#             prev.next = None
            
#         return slow
    
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#             # If the head doesn't exist, then the linked list is empty
#             if not head:
#                 return None
            
#             # Find the middle element for the list.
#             mid = self.findMiddle(head)
            
#             # The mid becomes the root of the BST.
#             node = TreeNode(mid.val)
            
#             # Base case when there is just one element in the linked list
#             if head == mid:
#                 return node
            
#             # Recursively form balanced BSTs using the left and right halves of the original list.
#             node.left = self.sortedListToBST(head)
#             node.right = self.sortedListToBST(mid.next)
#             return node
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ---------Convert to Array -> Rrecursion
        
#         listVals = []
        
#         while head:
#             listVals.append(head.val)
#             head = head.next
#         # print(listVals)
        
#         def sortedArrayToBST(listVals):
#             if not listVals:
#                 return

#             mid = len(listVals) // 2
#             tree_root = TreeNode(listVals[mid], None, None)
#             # print(tree_root)
            
#             tree_root.left = sortedArrayToBST(listVals[:mid])
#             tree_root.right = sortedArrayToBST(listVals[mid+1:])
            
#             return tree_root
        
#         return sortedArrayToBST(listVals)
  

        
        
        
        
        
        
        
        
        
        
        
        
        
