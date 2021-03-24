# 445. Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head:ListNode) -> ListNode:
        prev = None
        
        while head:
            next_node = head.next
            # reassign head.next to prev
            head.next = prev
            # Moving forward and update
            prev = head
            #mistake: head = head.next; ****head.next is prev now***
            head = next_node
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        carry = 0
        
        # *** In this case (unlinke LC2), we cannot initialize root = ListNode(0) because this will add a 0 at the end of our answer
        # root = n = ListNode(0)
        # ***We have to initialize root = None
        root = n = None

        while l1 or l2 or carry:
            
            v1, v2 = 0, 0
            
            if l1:
                v1 = l1.val
                l1 = l1.next
                
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            # ***Make sure the following statements are placed within the while loop, so the result linked list can be extended while addition proceeds
            carry, val = divmod(v1+v2+carry, 10)

            # ***Mistake: Instead of adding to the back, we want to add the value to the front (keep updating the head).
            n = ListNode(val)
            n.next = root
            root = n
            # result = self.reverseList(temp)
        
        return root
            
            
