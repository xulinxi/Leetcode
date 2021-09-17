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
    
 
   
   
   
      
  
  




