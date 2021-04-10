23. Merge k Sorted Lists

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        amount = len(lists)
        interval = 1
        
        def merge_sort(l1, l2):
            head = point = ListNode(0, None)
            
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next

                else:
                    point.next = l2
                    l2 = l1
                    l1 = point.next.next

                point = point.next
            
            if not l1:
                point.next = l2
            
            else:
                point.next = l1
            
            return head.next
        
        
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge_sort(lists[i], lists[i+interval])
            interval *= 2
            
#             
        # return lists[0] if len(lists) > 0 else lists (Note: return type is None)
        return lists[0] if len(lists) > 0 else None
        
        
        
        
        
        
        
        
        
        
        
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             # interval * 2 (step): calculating the iindex of new merged list
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval],lists)
#             # Increment the interval after every merge sort    
#             interval *= 2
#         return lists[0] if amount > 0 else None

#     def merge2Lists(self, l1, l2,lists):
#         head = point = ListNode(0)
#         while l1 and l2:
#             print(lists)
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
                
#                 # Swtich happens - l2 becomes rest of l1
#                 l2 = l1
#                 # l1 becomes next val of l2 because point.next = l2
#                 l1 = point.next.next
#             # point moves to the next val == the current compared list val 
#             # Note: point updates to/(always) point to the end of the sorting result/list(the most recent smallest val)
#             point = point.next
#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1
        
#         return head.next
