# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        # -----------Ref answers from tusizi--------
#         # @param {ListNode} head
#         # @return {ListNode}
#         prev = None
        
#         # As long as we have a node in our linked list
#         while head:
#             # We initialize the curr to head
#             curr = head
#             # head is traversing through to find the last node
#             head = head.next
#             # Connect the next node of curr to the previous node to reverse the linked list
#             curr.next = prev
#             # Move prev forwar after finish one reverse
#             prev = curr
#         return prev


# ----------(LC) Recursion------------

        # if head and head.next:
        #     n = self.reverseList(head.next)
        #     head.next.next = head
        #     head.next = None
        #     # ***Mistake: reverseList(self, node): has to return it
        # else:
        #     return head
        # return n
        
        # ---------Iterative---------------
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
            
        
        
