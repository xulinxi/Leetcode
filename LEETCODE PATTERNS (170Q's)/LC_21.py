# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # (Iteration) time: O(n + m); space: O(1) ---- Solution
        # Patterns/Methods:
        #     1. prehead: allows us to return the head of the merged list later
        #         ex: prev.next (reconnecting/merging)
        #     2. prev: points to the current node
        #         ex: l1 = l1.next (move on the the next node in the linked list)
            
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)
        prev = prehead
        
        # Bug: while l1 or l2:
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
                
            prev = prev.next
            
            # At least one of l2 and l2 can still have nodes at this point, so connect the non-null list to the end of the merged list
        prev.next = l1 if l1 else l2
        
        return prehead.next
            
        
