# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Step 1: Find mid
       
        
        # Step 2: if sub linkedList1 == reverse(sub linkedList2) -> if true :return True; else False
           
        # time: O(N); space: O(1)
        
        
        second_list = self.findMid(head)
        
        reversed_second_list = self.reverseLinkedList(second_list)
        
        # return head == reversed_second_list
        
        diff_count = 0
        l1, l2 = head, reversed_second_list
        
        while l1 or l2:
            if l1 != l2:
                diff_count += 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if diff_count > 1:
            return False
        
        return True
        
        
         # 1 -> 2 -> 3 -> 2 -> 1
            
                    # 1 -> 2 -> 3
        
        
    def findMid(head):  # find the mid node -> return mid node (2nd sub linkedList)
        
        # find the mid and cut the linked list into half
        
        
        
#         1 -> 2 -> 2 -> 1
#                   ^
#                              #
        
              # prev  
#         1 -> 2 -> 3 -> 2 -> 1
#                   ^
#                              #
        
        
        
        slow, fast = head, head
        
        prev = ListNode(None)
        prev.next = head
        
        while fast and fast.next:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next
            
        prev.next = None

        return slow
    
    
    def reverseLinkedList(head): # return a reversed linked list; reverse the linked list in place (avoid extra space)
#                 next
#            prev curr 
#            <-1  2 -> 3 -> None
        
        prev_node = None
        curr_node = head
#         # next_node = head.next
        
#     N <- 1 <- 2 <- 3 -> None
#                    p     n
#                          c  

 #     p c 
 # 1 2 3 None
        # Iterate through the linked list until the next == None
        while curr_node:
            
            # store next node val
            next_node = curr.next
            
            # disconnecting curr node to its curr next
            # point curr to prev
            curr.next = prev
            
            
#             # move on
# #             - prev to curr
#                 prev = curr
# #             - curr = next
#                 curr = next

        
        
        
        
        return head # reversed head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # ---- Solution
#         if head is None:
#             return True
        
#         # Find the end of first half and reverse second half.
#         first_half_end = self.end_of_first_half(head)
#         second_half_start = self.reverse_list(first_half_end.next)
        
#         # Check whether or not there's a palindrome
#         result = True
#         first_position = head
#         second_position = second_half_start
#         while result and second_position is not None:
#             if first_position.val != second_position.val:
#                 result = False
#             first_position = first_position.next
#             second_position = second_position.next
            
#         # Restore the list and return the result.
#         first_half_end.next = self.reverse_list(second_half_start)
#         return result
        
        
#     def end_of_first_half(self, head):
#         slow, fast = head, head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

#     def reverse_list(self, head):
#         previous = None
#         current = head

#         while current:
#             # 1. storing curr next node
#             next_node = current.next
#             # 2. (reversing step) reconnect curr.next to the previous node
#             current.next = previous
#             # 3. reset prev and curr (set prev to curr; set curr to next_node)
#             previous = current
#             current = next_node
#         return previous
        
        
        
        
