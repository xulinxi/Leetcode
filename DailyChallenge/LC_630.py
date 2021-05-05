# 630. Course Schedule III

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
    

#         pq = []
#         start = 0
#         # sorted_courses = sorted(courses, key = lambda c: c[1])
#         for t, end in sorted(courses, key = lambda c: c[1]):
#             start += t
            
#             # Always saved the courses (has traversed through) with the longest duration
#             heapq.heappush(pq, -t)
#             print(pq)
            
#             # if the course cannot be finished within the end time -> pop the pq's longest course
#             while start > end:
#                 start += heapq.heappop(pq)
#         return len(pq)
        
        # -------------------_(corrected)
        pq = []
        # count = 0
        
        time = 0
        # Note: The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on. 
        # Sort the courses by the lastDay
        sorted_courses = sorted(courses, key = lambda c: c[1])
        
        # 1. We traverse through the sorted courses, starting with the earliest last day
        # 1.2: (Check if to check if we can finish the course on time) the lastDay >= the duration + current time 
        # 2. Add the duration to time variable
        # 3. Find the next availble course, which has a larger number of lastDay than the current value of the time variable
        # 4. Increment the count variable for the number of courses we can take
        # 5. Make sure remove the course ***with the longest length (using priority queue)*** from the sorted_courses list: if we run out of the courses to add -> we reach the end
        for duration, lastDay in sorted_courses:
            
            heapq.heappush(pq, -duration)
            
            time += duration
            
            # Mistake: while lastDay < duration + time: (in the corrected version: time has been updated with added duration -> we can just directly compare the lastDay with time)
            while lastDay < time:
                time += heapq.heappop(pq)
                # count += 1
                # time += duration
                
        return len(pq)
    
        
        
        
        
        
        
        
        # ----------(wrong)
#         count = 0
        
#         time = 0
#         # Note: The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on. 
#         # Sort the courses by the lastDay
#         sorted_courses = sorted(courses, key = lambda c: c[1])
        
#         # 1. We traverse through the sorted courses, starting with the earliest last day
#         # 1.2: (Check if to check if we can finish the course on time) the lastDay >= the duration + current time 
#         # 2. Add the duration to time variable
#         # 3. Find the next availble course, which has a larger number of lastDay than the current value of the time variable
#         # 4. Increment the count variable for the number of courses we can take
#         # (5. Make sure remove the course from the sorted_courses list: if we run out of the courses to add -> we reach the end)
#         for duration, lastDay in sorted_courses:
            
#             if lastDay >= duration + time:
#                 count += 1
#                 time += duration
                
#         return count
            
                
                
            
                
            
