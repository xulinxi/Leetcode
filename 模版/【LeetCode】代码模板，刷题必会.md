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
      
  
  




