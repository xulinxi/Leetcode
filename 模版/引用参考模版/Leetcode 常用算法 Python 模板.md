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

## 区间 DP 对比 (Interval Dynamic Programming)

Notes on DP:

Tip: Top-Down DP vs. Bottom-Up DP

Top-Down DP, also known as Memoization DP, uses recursive function and memoization.

Bottom-Up DP, also known as Tabulation DP, uses iteration and DP array.


``` python
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    
    # 这里是区间DP
    for length in range(1, n+1):
        for l in range(n-length+1):
            r = l + length - 1
            dp[l][r] = s[l] == s[r] and )length < 3 or dp[l+1][r-1])
    
    return sum(map(sum, dp))
    
    n = len(s)
    dp = [[0] * (n) for _ in range(n)]
    
    for i in range(n): # 不要漏了这个初始化
        dp[i][i] = 1
    
    for l in range(1, n):
        for i in range(n-l):
            j = i + l
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                
   # n-最初公共子串
   return dp[0][-1]
   
   n = len(s)
   dp = [[0] * (n) for _ in range(n)]
   
   # 区间DP
   for length in range(1, n + 1):
        # l 是可以 range(n), length 又是从 1 开始的，所以 l 是range(n-length+1)
      for l in range(n-length+1):
          r = l+length-1
          if s[l] == s[r]:
              # 这里要确保 l < r
              dp[l][r] = dp[l+1][r-1] if l < r else 0
          else:
              dp[l][r] = 1+min(dp[l+1][r], dp[l][r-1])
      return dp[0][-1]
```
                  
### Resources:
[leetcode区间dp合集(from AcWing](https://www.acwing.com/blog/content/4802/)

### Similar Questions:
(LeetCode)\
[312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) and [its third solution](https://leetcode.com/problems/burst-balloons/solution/)
``` python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        # special case
        # Let N be the length of nums, and a be the element in nums. The coins we gain, no matter which one is burst, are always a * a * a, since all balloons are the same, except the last two balloons. For the last two balloons, one yields a * a * 1, and the other yields 1 * a * 1.
        if len(nums) > 1 and len(set(nums)) == 1:
            return nums[0] ** 3 * (len(nums)-2) + nums[0] ** 2 + nums[0]
        
        # handle edge case
        # nums[i - 1] and nums[i + 1] may be out of bounds for edge cases (leftmost and rightmost)
        nums = [1] + nums + [1]
        
        n = len(nums)
        
        # dp[i][j] represents maximum if we burst all nums[left]...nums[right], inclusive 
        # created a cube
        dp = [[0] * n for _ in range(n)]
        
        # do not include the first one and the last one
        # since they are both fake balloons added by ourselves and we can not burst them
        # left goes from n-1 -> 1 (-1 step)
        for left in range(n-2, 0, -1):
            # right goes from left -> n-2 (+1 step)
            for right in range(left, n-1):
                
                # find the last burst one in nums[left]...nums[right]
                for i in range(left, right + 1):
                    # nums[i] is the last burst one; gain is the coins that gained by pop ith balloon
                    gain = nums[left-1] * nums[i] * nums[right+1]
                    
                    # recursively call left side and right side; remaining is the coins gained by pop all ballons except the ith balloon.
                    remaining = dp[left][i-1]+dp[i+1][right]
                    # update
                    # note:dp[left][right] should be the optimzed coins gained by popping ballons in range[left, right]
                    dp[left][right] = max(remaining + gain, dp[left][right])
        
        # burst nums[1]...nums[n-2], exclusing the first one and the last one
        return dp[1][n-2]
         
```




























