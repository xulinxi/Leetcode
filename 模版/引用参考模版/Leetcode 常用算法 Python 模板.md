# reference link: https://zhuanlan.zhihu.com/p/98065331
(可能会有些改动）(Some changes might be added.)


## 小trick
- overlap 条件： start2 < end1 and end1 > start2
- key points:
  - DFS: Recursion, backtracking
  - BFS: Selection and label of Status

## 矩阵旋转 (Rotation Matrix)
* -> (i, j) -> (i, j): rotate 0 degree
* -> (i, j) -> (n-j-1, i): rotate 90 degrees
* -> (i, j) -> (n-i-1, n-j-1): rotate 180 degrees (or vertical flip)
* -> (i, j) -> (j, n-i-1): rotate 270 degrees

``` python
    for i in range(n):
        for j in range(n):
            if mat[i][j] != target[i][j]:
                c[0] = False
                
            if mat[i][j] != target[n-j-1][i]:
                c[1] = False
            
            if mat[i][j] != target[n-i-1][n-j-1]:
                c[2] = False
            
            if mat[i][j] != target[j][n-i-1]:
                c[3] = False
```
Notes: \
[Youtube Resource](https://www.youtube.com/watch?v=gCciKhaK2v8)\
j (col) is bounded by n - i - 1; i is increasing to the end (from left to right)\
i (row) is bounded by n // 2; because we are doing the swapping (only need to swap half positions)\
origin: matrix[i][j]\
left: matrix[n-1-j][i]\
bottom: matrix[n-1-i][n-1-j]\
right: matrix[j][n-1-i]

### Similar Questions:
(LeetCode)\
[48. Rotate Image](https://leetcode.com/problems/rotate-image/)

 ``` python
     class Solution"
        def rotate(self, matrix: List[List[int]]): -> None
            n = len(matrix)
            for i in range(n//2):
                for j in range(i, n-i-1):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n-j-1][i]
                    matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                    matrix[n-i-1][n-j-1] = matrix[j][n-i-j]
                    matrix[j][n-i-j] = temp
 ```






























