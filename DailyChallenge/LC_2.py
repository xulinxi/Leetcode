# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # ----------Ref from tusizi
        # l1 and l2 should be the heads for each list
        carry = 0
        
        # Initialize a new linked list for result
        root = n = ListNode(0)
        
        # As long as we have any value left in l1, l2 or carry:
        while l1 or l2 or carry:
            # Initialize a new linked list to store values
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next 
            carry, val = divmod(v1 + v2 + carry, 10)
            
            # Assign remainder val to the next node
            n.next = ListNode(val)
            n = n.next
            
        return root.next
            
