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

## 乐观锁 （Optimistic lock)

### Resources:
[Definition of Optimistic lock and pessimistic locking1](https://stackoverflow.com/questions/129329/optimistic-vs-pessimistic-locking)
[Definition of Optimistic lock and pessimistic locking1](https://leetcode-cn.com/circle/article/NbITSV/)

``` python
    class OptLock:
        def__init__(self, data): # data 即为需要并发安全的数据
            self.lock = threading.RLock()
            self.data = data
            self.version = 0
            
        def acquire(self): # 获取数据及版本号
            self.lock.acquire() # 该过程需要加锁是因为下面的语句不是原子操作
            data, ver = self.data, self.version
            self.lock.release*(
            return data, ver
            
        def update(self, data, version):  # 更新数据，需要传入以前的版本好
            self.lock.acquire()
            if version != self.version: # 当版本号与当前版本号不对应，返回 False
                self.lock.release()
                return False
            else: # 否则返回 True
                self.data = data
                self.version += 1
                self.lock.release()
                return True
```          

### Similar Questions:
(LeetCode)\
[1117. Building H2O](https://leetcode.com/problems/burst-balloons/) and [its third solution](https://leetcode.com/problems/building-h2o/) and [other solution 1](https://newdee.gitbook.io/leetcode/1117.building_h2o), [other solution 2](https://www.cnblogs.com/niuyourou/p/12446032.html)

#### Concepts:
* [Semaphore](https://pythontic.com/multithreading/synchronization/semaphore)
  - A semaphore is a synchronization construct.
  - Semaphore provides threads with synchronized access to a limited number of resources.
  - A semaphore is just a variable. The variable reflects the number of currently available resources. For example, a parking lot with a display of number of available slots on a specific level of a shopping mall is a semaphore.
  - The semaphore is associated with two operations – acquire and release.
  - When one of the resources synchronized by a semaphore is "acquired" by a thread, the value of the semaphore is decremented.
  - When one of the resources synchronized by a semaphore is "released" by a thread the value of the semaphore is incremented.
* [Barrier Objects in Python](https://www.geeksforgeeks.org/barrier-objects-python/)
  - Each thread calls wait() function upon reaching the barrier. The barrier is responsible for keeping track of the number of wait() calls. If this number goes beyond the number of threads for which the barrier was initialized with, then the barrier gives a way to the waiting threads to proceed on with the execution. All the threads at this point of execution, are simultaneously released.
* [.wait() method in Python](https://www.geeksforgeeks.org/python-os-wait-method/)
  - a process to wait for completion of a child process

``` python
  from threading import Barrier, Semaphore
  class H2O:
      def __init__(self):
          self.b = Barrier(3)
          self.h = Semaphore(2)
          self.o = Semaphore(1)

      def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
          self.h.acquire()
          self.b.wait()

          # releaseHydrogen() outputs "H". Do not change or remove this line
          releaseHydrogen()
          self.h.release()

      def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
          self.o.acquire()
          self.b.wait()

          # releaseOxygen() outputs "O". Do not change or remove this line
          releaseOxygen()
          self.o.release()   
```

## 矩阵转置 （Transpose Matrix)

[Matrix Transpose](https://www.cuemath.com/algebra/transpose-of-a-matrix/)
* The transpose of a matrix is obtained by changing its rows into columns and its columns into rows.

(Only works with M*M matrix)
``` python
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] ==  matrix[i][j], matrix[j][i]
```

### Similar Questions:
(LeetCode)\
[867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

``` python
    class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    
        # # Only works for N*N matrix
        # for i in range(len(matrix)):
        #     # * Note: we don't want to do 2 swaps (back to original)
        #     for j in range(i, len(matrix)):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix
        
        R, C = len(matrix), len(matrix[0])
        
        tMatrix = [[None] * R for _ in range(C)]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                tMatrix[c][r] = val
        return tMatrix
```       

## Tree Algorithm 

## Binary Indexed Tree (BIT) or Fenwick Tree 树状数组

[Binary Indexed Tree or Fenwick Tree](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)

(Only works with M*M matrix)
``` python
    class BIT:
        def __init__(self, n):
            self.n = n + 1
            self.sums = [0] * self.n
            
        def update(self, i, delta):
            while i < self.n: # i 不能为 0！！！
                self.sums[i] += delta
                i += i & (-1) # = i & (~i + 1) 用于遗踪最低位的 1
                
        def prefixSum(self, i):
            res = 0
            while i > 0:
                res += self.sums[i]
                i -= i & (-i)
            return res
            
        def rangeSum(self, s, e):
            return self.prefixSum(e) - self.prefixSum(s - 1)
```

### Similar Questions:
(LeetCode)\
[308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) and [its solution](https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/1332920/Python-Binary-Indexed-Tree-Clean-and-Concise)

``` python
    class BIT:
    def __init__(self, size): # One-based indexing
        self.bit = [0] * (size + 1)
    
    def getSum(self, idx):
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= idx & -idx
        return ans
    
    def getSumRange(self, left, right): # right exclusive
        return self.getSum(right) - self.getSum(left - 1)
    
    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & -idx


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.bits = [BIT(n) for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                diff = matrix[r][c] - self.bits[r].getSumRange(c+1, c+1)
                self.bits[r].update(c+1, diff)
        
        self.matrix = matrix        

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        diff = val - self.bits[row] .getSumRange(col + 1, col + 1)
        self.bits[row].update(col + 1, diff)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            ans += self.bits[r].getSumRange(col1 + 1, col2 + 1)
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

```

## Binary Search Tree

[Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.

``` python
    class Node(object):
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
    
    class BST():
        def __init__(self):
            self.root = None
            
        def insert(self, data):
            def__insert(node):
                if not node:
                    return Node(data)
                
                if data < node.val:
                    node.left = __insert(node.left)
                elif data > node.val:
                    node.right = __insert(node.right)
                return node
            self.root = __insert(self.root)
            
        def search(self, data, parent=None):
            if data < self.data:
                if self.left is None:
                    return None, None
                return self.left.search(data, self)
            elif data > self.data:
                if self.right is None:
                    return None, None
                return self.right.search(data, self)
            else:
                return self, parent
                
    class Node(object):
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
        
        def insert(self, data):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                        
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
                
        def search(self, data, parent = None):
            if data < self.data:
                if self.left is None:
                    return None, None
                return self.left.search(data, self)
            
            elif data > self.data:
                if self.right is None:
                    return None, None
                return self.right.search(data, self)
            else:
                return self, parent  
   
```  

### Similar Questions:
(LeetCode)\
[700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) 

``` python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def searchBST(self, root: TreeNode, val: int) -> TreeNode:
            if not root:
                return None
            elif root.val < val:
                return self.searchBST(root.right, val)
            elif root.val > val:
                return self.searchBST(root.left, val)
            elif root.val == val:
                return root

```


## Trie

[Trie](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

``` python
    import collections
    class TrieNode():
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.isEnd = False
    
    class Trie():
        def __init__(self):
            self.root = TrieNode()
        
        def insert(self, word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.isEnd = True
            
        def search(self, word):
            node = self.root
            for w in word:
                if w not in node.children:
                    return False
                node = node.children[w]
            return node.isEnd
```

or

``` python
import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isEnd = True        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```








































