# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
     # ------Approach 2

    
        if head is None:
            return True
        
        # Find the end of the first alf and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        # Check whether or not there's a palindrome
        result = True
        first_position = head
        second_position = second_half_start
        
        while result and second_position:
            if first_position.val != second_position.val:
                result = False
            
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result
        first_half_end.next = self.reverse_list(second_half_start)
        return result
    
    
        
    def end_of_first_half(self, head):
            fast = head
            slow = head
            
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
    def reverse_list(self, head):
        previous = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
            
        return previous
            
            
        
        
        
        
       # ----Approach 1
#         val = []
#         curr = head
#         while curr:
#             val.append(curr.val)
#             curr = curr.next
            
#         return val == val[::-1]
    
    
  
    
    
