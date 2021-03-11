# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
    
    # Recursive Method------------------------------------------------------
        # !!!Base case: no more number left!!!
        if not nums:
            return 
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index], None, None)

        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])
        
        return root
        

        
