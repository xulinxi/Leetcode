# 203. Remove Linked List Elements


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(0, None)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next

            else:
                prev = curr
            curr = curr.next
            
        return dummy.next
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = ListNode(0, None)
#         dummy.next = head
#         prev = dummy
#         curr = head
        
#         while curr:
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#             curr=curr.next
              
#         return dummy.next
                
