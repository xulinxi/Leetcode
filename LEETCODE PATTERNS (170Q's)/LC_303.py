# 303. Range Sum Query - Immutable

class NumArray:

    # [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    
#     [0,0]: -2 
#     [0,1]: -2 = [0, i-1] + numArray(i)
#     [0,2]: 1 = [0, i-1] + numArray(i)
#     [0,3]: -4 = [0, i-1] + numArray(i)
        
    
#     dummy = NumArray = [-2, 0, 3, -5, 2, -1]
#                         [-2, 0 + sum(index 1-1) = 0 + (-2) ... ]
#                         [-2, -2, 1, -4, -2, -3]
            
#      [2, 5] = [3, -5, 2, -1] = [0, 5] - [0, 1] = [0, end index] - [0, start index-1] = -3 - (-2) = 1
    
    
#     return dummy[end_index] - dummy[start-1 if start > 0 else 0]
    
    # time: O(N); space: O(N)
    

    
    def __init__(self, nums: List[int]):

        self.sums = nums    # [1,2,3,4]
        for i in range(1, len(self.sums)): # 2,3,4
            self.sums[i] = self.sums[i-1] + self.sums[i] # sums[3] = sums[3-1] + sums[3] = 6 + 4 = 10
                                          # sums [1,3,6,10   ]

    def sumRange(self, left: int, right: int) -> int: #[0,3]
        if left == 0:
            return self.sums[right] # 10
        else:
            return self.sums[right] - self.sums[left-1] # sums[3] - sums[0] = 10-1 = 9 == expected 9
        
        # return self.sums[right] - self.sums[left-1 if left > 0 else 0]n #[0, 5]
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    # (Dynmic Programming/Cache) time: O(n); space: O(n) ---- ChrisZhang12240
    
#     def __init__(self, nums: List[int]):
#         self.dp = nums
#         for i in range(1, len(nums)):
#             self.dp[i] += self.dp[i-1]

#     def sumRange(self, left: int, right: int) -> int:
#         return self.dp[right] - (self.dp[left-1] if left > 0 else 0)
    
#     # (Dynmic Programming/Cache) time: O(n); space: O(n) ---- jianchao-li
#     def __init__(self, nums: List[int]):
#         """"
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.accu = [0]
#         for num in nums:
#             self.accu += self.accu[-1] + num,
            
#     def sumRange(self, left: int, right: int) -> int:
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return self.accu[right + 1] - self.accu[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
