# 24. Swap Nodes in Pairs


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # Approach 1: Recursove Approach
#         # If the list has no node or has only one node left
#         if not head or not head.next:
#             return head
        
#         # Nodes to be swapped
#         first_node = head
#         second_node = head.next
        
#         # In the base case. first_node.next, therefore in recursion, we pass second_node.next in a recursive function
#         first_node.next = self.swapPairs(second_node.next)
#         second_node.next = first_node
        
#         return second_node

# -------------# Approach 2: Iterative Approach----------------
        # Create a dummy node; dummy -> head; dummy is the prev_node
        dummy = ListNode(-1)
        dummy.next = head
        
        # Mistake: dummy = prev_node
        prev_node = dummy
        
        while head and head.next:
            
            # Nodes to swapped
            first_node = head
            second_node = head.next
            
            # Swapping
            # Missing:reassigning prev_node -> failed to remember the head in the return step
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # (Move forward) Reinitializing the prev_node, head (will be the first _node), second_node
            prev_node = first_node
            head = prev_node.next
            # second_node = head.next will be initialized later in the loop
            
        return dummy.next
    
        
        
