# (Biweekly Constest #1) 03062021
# 1779. Find Nearest Point That Has the Same X or Y Coordinate

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        # Goal: Find the index for the first smallest distance:
        # 1. Loop through the points list
        # 2. keep track/update smallest Manhattan distance
        # 3. return the index of the 1st smallest Manhanttan distance (only update the min distance when the distance is smaller than current min distance)
        min_dis = 10000
        # index = 0 -> if index = 0, we need to have another else statement beneath the for loop to catch an edge case where there's only one invalid point in the list
        # Instead, if index = -1, index will not be updated unless there's at least a valid point!
        index = -1
        for i, (a,b) in enumerate(points):
            dx = abs(x-a)
            dy = abs(y-b)
            
            # min_dis = 10000  -> can't be renewed everytime -> must be set outside of the loop
            # Note: when x == a, x-a == 0
            # Therefore, when x == a or y == b, we calculate their Manhanttan distance
            # Two if statements can be implement together with "and"
            # print(i, dx + dy)
            if dx * dy == 0 and dx + dy < min_dis:
                
                min_dis = dx + dy
                index = i
                # print(i, index, min_dis)
                
        # return i -> got a wrong answer because always get the last index....
        return index
                
                
        
 # Test cases          
# 5
# 1
# [[1,1],[6,2],[1,5],[3,1]]
# 3
# 4
# [[1,2],[3,1],[2,4],[2,3],[4,4]]
                
        
        
        
        
        
        
        
        
        
#         # ----------------------------------------------------------------
#         # *** Note: return index! not the smallest distance; can't create another list because we need to find out the index, not the min distance
# (Wrong answer)
#         # Step 1: Select out the points with a = x or b = y:
#         valids = []

#         for i in range(len(points)):
#             if points[i][0] == x or points[i][1] == y:
#                 valids.append(points[i])
#                 valids.append(i)
#                 # print(x, y, i, "valid:", points[i])
        
#         # print(len(valids))
#         if len(valids) == 1:
#             return 0
#         elif len(valids) > 1:
#             min = 100000
#             index = 0
#             for i in range((len(valids)//2) - 1):
#                 current_dis = abs(valids[i][0] - valids[i+2][0]) + abs(valids[i][1] - valids[i+2][1])
#                 # print(valids[i], valids[i + 1], current_dis)
#                 if current_dis < min:
#                     min = current_dis
#                     index = i
#             return i
#         else:
#             return -1


# (An answer from discussion) ------------------------
#         smallest, index = math.inf, -1
#         for i, (r, c) in enumerate(points):
#             dx, dy = x - r, y - c
            
#             if dx * dy == 0 and abs(dx) + abs(dy) < smallest:
#                 # print(r,c)
#                 # print(dx, dy)
#                 smallest = abs(dx) + abs(dy)
                
#                 index = i
#         return index 
            
        
