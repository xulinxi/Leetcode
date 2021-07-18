# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Note: fast is reassigned within the while loop -> when fast at node 5, slow at node 3
        # slow = slow.next
        
        return slow
