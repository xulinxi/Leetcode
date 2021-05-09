# 1851. Minimum Interval to Include Each Query

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
     
    #     referece: https://www.youtube.com/watch?v=5hQ5WWW5awQ
        intervals.sort()  # [[1,4],[2,4],[3,6],[4,4]]
        
        minHeap = []
        res, i = {}, 0
        
        for q in sorted(queries): # [2, 3, 4, 5]
            
            # Step 1: Check the left bound (add to minHeap) with calulcated interval
            # intervals[i][0]: start of the interval; q: each query; 
            # intervals[i][0] <= q means: checking if the query falls within the interval 
            # (the query must be after the start of the interval)
            while i < len(intervals) and intervals[i][0] <= q: 
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r)) # minHeap: [(4,4),(2,4),(4,6),(1,4)] => [(1,4),(2,4),(4,4),(4,6)]
                i += 1
            
            # Step 2: Check the right bound (pop from minHeap)
            # minHeap[0][1]: always is: the end of the shortest interval
            # heapq.heappop(heap):
            # Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
            while minHeap and minHeap[0][1] < q: 
                heapq.heappop(minHeap) 
            
            res[q] = minHeap[0][0] if minHeap else - 1 
        
        return [res[q] for q in queries]
        
        
        
        
        
        
        
        
        
        # -----------------------------
        
#         intervals = sorted(intervals)[::-1] # [[4, 4], [3, 6], [2, 4], [1, 4]]
#         # print(intervals)
        
#         h = []
#         res = {}
        
#         for q in sorted(queries): # 5 -> 4 -> 3 -> 2
#             while intervals and intervals[-1][0] <= q:
#                 i, j = intervals.pop()
#                 if j >= q:
#                     heapq.heappush(h, [j - i + 1, j])
#             while h and h[0][1] < q:
#                 heapq.heappop(h)
#             res[q] = h[0][0] if h else -1
#         return [res[q] for q in queries]
