# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # Iterate through my link list: *** checking if curr and curr.next (time: O(n); space: O(1))
            # Create a pointer: curr -> compare curr.val and curr.next.val:
            #                             - if equal: (reconnect/deleting) curr.next = curr.next.next 
            #                             - if not: (move on) curr = curr.next
                
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # curr_value = 0
#         prev, curr = head, head
        
#         while curr and curr.next:
#             if curr.val == curr.next.val:
#                 prev.next = curr.next
#                 # curr = curr.next
#             elif curr.val != curr.next.val:
#                 prev = curr
#             curr = curr.next
    
    
    
    
#     # ---- Mine
#         curr = head
        
#         while curr and curr.next:
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
            
#         return head
            
            
        
