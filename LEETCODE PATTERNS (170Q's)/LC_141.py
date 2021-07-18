# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
#         # two pointers: slow, fast
        
#         # Iterate through the list using while loop: (while fast, fast.next)
#         #     if we have a cycle (loop): slow and fast will meet -> slow == fast -> return True
#         #     if no cycle: (stops when we find a None node) -> return False (outside of the loop)
        
# #              |
# #         1 -> 2 -> 3 -> 4 -> 5 (odd)
# #  slow:                      *
# #  fast:                      **          
        
            
# #              |
# #         1 -> 2 -> 3 -> 4 -> 5 -> 6 (even)



#  # 1-> 2-> 3 -> None

#     # time: O(n); space: O(1)
    
#         # Two pointers initialization:
#         slow, fast = head, head     # 1, 1
        
#         # Iterate through the given linked list
#         while fast and fast.next:   # T, T
#             # Case1: loop -> stops when slow meets fast -> return True
#             slow = slow.next # move 1 step    
#             fast = fast.next.next # move 2 steps  
#             if slow == fast:
#                 return True
            

        # # Case2: no loop -> stops when reach a None (out of while loop) -> return False
        # return False
            
    
             
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # (Floyd's Cycle Finding Algorithm) time: O(n); space: O(1) ---- Mine
#         slow, fast = head, head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#             # else: Note: Mistake: should be before checking a cycle
#             #     slow = slow.next
#             #     fast = fast.next.next
#         return False
            
