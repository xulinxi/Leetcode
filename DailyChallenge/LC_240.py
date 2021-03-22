# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # ---------_Binary Searxh------------------
       
    
    
    
# -----------(Failed)Try to take advantage of the sorted numbers and use brute force----
#         max_row_index = 0
#         max_col_index = 0
        
#         # 1*1 array
#         if len(matrix) == 1 and len(matrix[0]) == 1:
#             if matrix[max_row_index][max_col_index] == target:
#                 return True

#         else:
            
#             # 1-D array (row)
#             if len(matrix) == 1 and len(matrix[0]) > 1:
#                 max_row_index = 1
#             # 1-D array (1 column)
#             elif len(matrix[0]) == 1 and len(matrix) > 1:
#                 max_col_index = 1
            
#             # regular 2-D array
#             # *** Note 1: When the target is too large, we can never find it:
#                 # stop when we run out of things (row/column) to check***
#             # ***Note 2: Make sure the index must be less than the len***
#             while matrix[max_row_index][0] <= target and max_row_index < len(matrix) - 1:
#                 max_row_index += 1

#             while matrix[0][max_col_index] <= target and max_col_index < len(matrix[0]) - 1:
#                 max_col_index += 1 

#             for i in range(max_row_index):
#                 for j in range(max_col_index):
#                     if matrix[i][j] == target:
#                         return True
#             return False
            
            
            
            # ---------Brute Force----------
            # for i in range(len(matrix)):
            #     for j in range(len(matrix[0])):
            #         if matrix[i][j] == target:
            #             return True
            # return False
            
# ---------Brute Force (take advantage of sorted array)----------
            for i in range(len(matrix)):
                if matrix[i][0] <= target and matrix[i][len(matrix[0])-1] >= target:
                    for j in range(len(matrix[i])):
                        if matrix[i][j] == target:
                            return True
            return False
