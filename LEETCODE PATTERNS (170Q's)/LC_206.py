# 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # dummy = ListNode(0, None)
        # Mistake: prev = ListNode(0, None)
        prev = None
        curr = head
        # dummy.next = head
        
        
        
        while curr:
            next_node = curr.next # Remember the current next node
            curr.next = prev # Reversing step
            
            prev = curr 
            curr = next_node
        
        # Missing step:
        head = prev    
        # return dummy.next
        return head
