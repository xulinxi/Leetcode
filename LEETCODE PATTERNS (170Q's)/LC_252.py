# 252. Meeting Rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals = sorted(intervals)
        # print(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        else:
            return True
        
        
