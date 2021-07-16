# 827. Making A Large Island

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
      
    
    # grid = [[1,0],[0,1]]
    
#     1 0
#     0 1
    
    
#     2 2 0 
#     0 0 0    
#     3 3 0 
    
    
    # Goal: find the 0 where it's connecting with the max numbers of area (many times means the 0 should probably connects with more islands).
    
    
#     # loop through each number
#     1st loop: indexing different islands
        
#     Mapping: {
#     index: area
#     2: 2
#     3: 2
#     }
    
#     # (TODO: which 0 connects with the most islands and achieve the largest area) -> 2nd loop
    
#     0 (0, 2)
#     max = 0
#     2 + 1 = 3 = max(max, area of neighboring islands + 1) = max
    
#     0 (1, 0)
#     island2 (area 2)
#     island3 (area 2)
#     total: (changing this 0 ) = i2 + i3 + 1 = 5 = curr_area
#     max = max(max, curr_area) = 5
    
#     return max

    # helpers:
    #     - neighbors (find connecting lands) -> check 4 directions
    #     - search helper (move to the next valid land; keep count of area)
    
    # N = r = c
    N = len(grid)
    
    # 2 helpers:
        # - neighbors (find 4 directions)
        # - search
    
    def neighbor(r, c): # return at most 4 valid (lands) neighbors 
        
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < N and 0 <= nr < N:
                yield nr, nc
        
    def search(r, c, index): # search for neighbors and find out the area of the islands -> return area of this islands
        ans = 1
        grid[r][c] = index
        
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                ans += search(nr, nc, index)
                # 1 + 1 = 2 + 1 = 3
        return ans
        #   * 
        # 2 1 *
        # 1 0
    
    # Mapping (index: area)
    islands_area = {}
    index = 2  # > 1: visited islands; == 1: unvisited islands
    
    
    
    # 2 loops

    # 1st loop: indexing different islands == 1
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                islands_area[index] = search(r, c, index)
                index += 1
                
        
    ans = max(area.values() or [0])
    
#     1 0 0 0 1
#     1 1 0 0 0
#     1 0 0 0 1
#     1 0 0 0 0
    
#     6
    
    # 2nd loop: finding the 0 can connect to the most lands
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                seen = {grid[nr][nc] for nr, nc in neighbors(r,c) if grid[nr][nc] > 1}
                ans = max(ans, 1 + sum(area[i] for i in seen))
                
    return ans
                
    time: O(n^2); space:(n^2/2 = n^2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#         # (Component Sizes w Hash Map) time: O(n^2); space: O(n^2) ---- Solution
        
#         # N = row = col since n by n matrix grid
#         N = len(grid)
        
#         # get neighbors
#         def neighbors(r, c):
#                             # left.     right.    up       down
#             for nr, nc in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1) ):
#                 if 0 <= nr < N and 0 <= nc < N:
#                     yield nr, nc
        
#         # dfs, get total area
#         def dfs(r, c, index):
#             ans = 1
#             grid[r][c] = index
            
#             for nr, nc in neighbors(r, c):
#                 if grid[nr][nc] == 1:
#                     ans += dfs(nr, nc, index)
                    
#             return ans
        
#         # mapping for index(each island): area
#         area = {}
        
#         # index starts w/ 2 (if we see a 1, we know we encounter a new island)
#         index = 2
        
#         # changing island index
#         for r in range(N):
#             for c in range(N):
#                 if grid[r][c] == 1:
                    
#                     # set the current island index = its max area
#                     area[index] = dfs(r, c, index)
#                     index += 1
                    
#         ans = max(area.values() or [0])
        
#         for r in range(N):
#             for c in range(N):
#                 if grid[r][c] == 0:
                    
#                     # grid[nr][nc] > 1 -> checking the island index (the islands) around this 0
#                     seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    
#                     # print([area[i] for i in seen])
#                     ans = max(ans, 1 + sum(area[i] for i in seen))
        
#         return ans
                
