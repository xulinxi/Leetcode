# reference link: https://blog.csdn.net/fuxuemingzhu/article/details/101900729

# Binary Search

## Practice Question(s): 
### (Leetcode) 
#### [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Other Resources:
花花酱的二分查找专题视频：https://www.youtube.com/watch?v=v57lNF2mb_s

Template:
Range: [l, r) 左闭右开

其中f(m)函数代表找到了满足条件的情况，有这个条件的判断就返回对应的位置，如果没有这个条件的判断就是lowwer_bound和higher_bound.

```python
def binary_search(l, r):
  while l < r:
    m = l + (r - l) // 2
    if f(m):  # 判断找了没有，optional
      return m
    if g(m):
      r = m.  # new range [l, m)
    else:
      l = m + 1 # new range [m+1, r)
  return l  # or not found
  ```
  
  lower bound: find index of i, such that ```A[i] >= x ```
  
  ``` python
  def lower_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid
    return left
  ```
  
  upper bound: find index of i, such that ```A[i] > x```
  
  ``` python
  def higher_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] <= target:
        left = mid + 1
      else:
        right = mid
    return left
   ```
    
   
   For example, [LeetCode 69](https://leetcode.com/problems/sqrtx/) and [its solution](https://blog.csdn.net/fuxuemingzhu/article/details/79254648).
   
   ``` python
   class Solution(object):
      def mySqrt(self, x):
          """
          :type x: int
          :rtype: int
          """
          left, right = 0, x + 1
          #[left, right)
          while left < right:
              mid = left + (right - left) // 2
              if mid ** 2 == x:
                  return mid
              if mid ** 2 < x:
                  left = mid + 1
              else:
                  right = mid
          return left - 1
   ```
   
   # Sorting
   
   C++的排序方法，使用sort并且重写comparator，如果需要使用外部变量，需要在中括号中放入&。

   ## Practice Question(s): 
   ### (Leetcode) 
   #### [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
   
   ``` C++
   class Solution {
   public:
      string frequencySort(string s) {
          unordered_map<char, int> m;
          for (char c : s) ++m[c];
          sort(s.begin(), s.end(), [&](char& a, char& b) {
              return m[a] > m[b] || (m[a] == m[b] && a < b);
          });
          return s;
      }
   }; 
   ```
   
   # BFS
   
   下面的这个写法是在一个邻接矩阵中找出离某一个点距离是k的点。

   ## Practice Question(s): 
   ### (Leetcode) 
   #### [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
   来自文章：[【LeetCode】863. All Nodes Distance K in Binary Tree 解题报告（Python）](https://blog.csdn.net/fuxuemingzhu/article/details/82709619)
   
   ``` python
   # BFS
   bfs = [target.val]
   visited = set([target.val])
   for k in range(K):
      bfs = [y for x in bfs for y in conn[x] if y not in visited]
      visited |= set(bfs)
   return bfs
   ```
   
    #### [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
    在BFS中保存已走过的步，并把已经走的合法路径删除掉。
    (Save the visited steps, and delete valid path)
    
   ``` python
    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """
            wordset = set(wordList)
            bfs = collections.deque()
            bfs.append((beginWord, 1))
            while bfs:
                word, length = bfs.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordset and newWord != word:
                            wordset.remove(newWord)
                            bfs.append((newWord, length + 1))
            return 0
   ```  
   
   #### [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) 
   [(solution)](https://blog.csdn.net/fuxuemingzhu/article/details/82926674)
   使用优先级队列来优先走比较矮的路，最后保存最高的那个格子的高度。
   (Use priority queue to select the lower level first, and save the height of the tallest block.)
    
    
   ``` python
    class Solution(object):
        def swimInWater(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            n = len(grid)
            visited, pq = set((0, 0)), [(grid[0][0]), 0, 0]
            res = 0
            while pq:
                T, i, j = heapq.heappop(pq)
                res = max(res, T)
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                if i == j == n - 1:
                    break
                for dir in directions:
                    x, y = i + dir[0], j + dir[1]
                    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                        continue
                    heapq.heappush(pq, (grid[x][y], x, y))
                    visited.add((x, y))
            return res
   ```    
  
   #### [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) 
   [(solution)](https://blog.csdn.net/fuxuemingzhu/article/details/82939203)
   需要找出某顶点到其他顶点的最短路径。出发顶点不是确定的，每个顶点有可能访问多次。使用N位bit代表访问过的顶点的状态。如果到达了最终状态，那么现在步数就是所求。这个题把所有的节点都放入了起始队列中，相当于每次都是所有的顶点向前走一步。
   Note: Need to find the shortest path that from each node to other nodes
      - Starting node is uncertain; each node can be visited more than once
      - Remember the visited node state -> if reach the final state -> get current steps
    
    
   ``` python
    class Solution(object):
        def shortestPathLength(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: int
            """
            N = len(graph)
            que = collections.deque()
            step = 0
            goal = (1 << N) - 1
            visited = [[0 for j in range(1 << N)] for i in range(N)]
            
            for i in range(N):
                que.append((i, 1 << i))
            
            while que:
                s = len(que)
                
                for i in range(s):
                    node, state = que.popleft()
                    if state == goal:
                        return step
                    if visited[node][state]:
                        continue
                    visited[node][state] = 1
                    for nextNode in graph[node]:
                        que.append((nextNode, state | (1 << nextNode)))
                step += 1
           
            return step
   ```  
   
#### [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) 
   [(solution)](https://blog.csdn.net/fuxuemingzhu/article/details/81022170)
   多叉树的层次遍历，这个BFS写法我觉得很经典。适合记忆。
   (Classic BFS solution -> suitable to be memorized)
    
   ``` python
   """
   Definition for a Node.
   Class Node(object):
      def __init__(self, val, children):
          self.val = val
          self.children = children
   """
   
    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: Node
            :rtype: List[List[int]]
            """
            res = []
            que = collections.deque()
            que.append(root)
            
            while que:
                level = []
                size = len(que)
                for _ in range(size):
                    node = que.popleft()
                    if not node:
                        continue
                    level.append(node.val)
                    
                    for child in node.children:
                        que.append(child)
                if level:
                    res.append(level)
            return res
   ```     
   
   
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
            
            
            
            
            
            
            
            
 
   
   
   
      
  
  




