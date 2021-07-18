# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, None)
        # previous = ListNode(0, None)
        curr = head
        prev = dummy
        dummy.next = head
        # prev.next = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                # curr = curr.next
            # Note/Mistake: What if not the same -> move on to the next node
            else:
                prev = curr
            curr = curr.next
                
        return dummy.next
        
