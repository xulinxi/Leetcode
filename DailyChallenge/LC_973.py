# 973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        # √(x1 - x2)^2 + (y1 - y2)^2 = sqrt(x1 - x2)**2 + (y1 - y2)**2 -> sqrt((x1)**2 + (y1)**2)
        # [1,3] -> sqrt(1^2 + 3^2) = sqrt(10)
        # [-2,2] ->  sqrt(2^2 + 2^2) = sqrt(8)
        
        # points = [(sqrt(10),[1,3]),(sqrt(8),[-2,2])] -> sort it 
        
        # return k closest (i for i in k; first k points[i][1]) 
        
#         time: O(nlogn + n) = O(nlogn)
#         space: O(n)
    
        # Calculating distance for each point
        for i in range(len(points)):   # 0, 1, 2; [3,3],[5,-1],[-2,4]
            points[i] = (sqrt((points[i][0])**2 + (points[i][1])**2), points[i])
            
        # [(dis0, []), (dis1, []), (dis2, [])]    
        
        points.sort()
        
        # points[i][1] === point's coordiate
        
        return [points[i][1] for i in range(k)]
            
        
        
        # [[3,3],[5,-1],[-2,4]], k = 2
        
#         points = [(distance0,[3,3]),(distance1,[5,-1]),(distance2,[-2,4])]
        
        
#         [points[0][1], [points[1][1] ] = [[3,3],[5,-1] ]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ---- Mine
        
#         # √(x1 - x2)^2 + (y1 - y2)^2 
#         # when (x2, y2) = (0, 0)
#         # ->  √(x1)^2 + (y1)^2 
        
#         for i in range(len(points)):
#             # print(points[i][0])
#             # print((points[i][0])^2 )
#             # print((points[i][0])^2 + (points[i][1])^2)
#             # print(sqrt((points[i][0])^2 + (points[i][1])^2))
#             distance = sqrt((points[i][0])**2 + (points[i][1])**2)
#             points[i] = (distance, points[i])
            
#         points.sort()
        
#         # result = [points[i][1] for i in range(k)]
#         return [points[i][1] for i in range(k)]
