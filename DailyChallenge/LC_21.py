# 21. Merge Two Sorted Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        dummy = ListNode(0, None)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
        
        # if any remains after one list runs out
        curr.next = l1 or l2 
        
        # note: return head_point.next because head_pointer is None
        return dummy.next
        
        
        
        
        # -------(Wrong)
#         if l1 or l2:
#             if l2.val <= l1. val:
#                 head = l2
#                 l2 = l2.next
#             else:
#                 head = l1
#                 l1 = l1.next
                
#         while l1 and l2:
#             if l2.val <= l1. val:
#                 head = l2
#                 l2 = l2.next
#             else:
#                 head = l1
#                 l1 = l1.next
            
            
        
            
