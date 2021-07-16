# 1428. Leftmost Column with at Least a One

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        # (Start at Top Right, Move Only Left and Down) 
        row, col = binaryMatrix.dimensions()
        curr_row, curr_col = 0, col - 1
        
        # Bug: while curr_row < row - 1 and col >= 0:
        while curr_row < row and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 1: # if 1 (go left)
                curr_col -= 1
            else: # if == 0 (go down)
                curr_row += 1
            # if binaryMatrix.get(curr_row, curr_col) == 0: # if 1 (go left)
            #     curr_row += 1
            # else: # if == 0 (go down)
            #     curr_col -= 1
                
            # if stay in last col -> curr_col == (no change) col -1 => return -1
            # if curr_col != col - 1 (even when there is only one 1 in the last col and last row, the curr_col will be added by 1)
        # Bug: return curr_col if curr_col != col - 1 else -1
        return curr_col + 1 if curr_col != col - 1 else -1
        

        
        # (Wrong) Too many calls ---- Mine
#         # Bug: row, col = BinaryMatrix.dimensions()
#         row, col = binaryMatrix.dimensions()
#         row_sum = 0
        
#         for i in range(col):
#             for j in range(row):
#                 # Bug: row_sum += BinaryMatrix.get(j, i)
#                 row_sum += binaryMatrix.get(j, i)
            
#             # Note:  return the index (0-indexed) of the leftmost column with AT LEAST a 1 in it. (from testing)
#             # This could be a clarifying question for the interview.
#             if row_sum >= 1:
#                 return i
#         else:
#             return -1
        
