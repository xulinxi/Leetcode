# 912. Sort an Array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
    
    # -------Merge Sort (Divide and conquer)-------------
    # ---（refer to junaidmansuri's discussion-merge sort)
        def mergeSort(nums):
            if len(nums) == 1: 
                return nums
                
            else:
                left_merge = mergeSort(nums[:len(nums)//2])
                # *** end index should be exclusive whole start index is inclusive!!
                right_merge = mergeSort(nums[len(nums)//2:])
            return merge(left_merge, right_merge)
            
            
            
        def merge(left, right):
            left_len = len(left)
            right_len = len(right)
            S, curr_left, curr_right = [], 0, 0
            
            while curr_left < left_len and curr_right < right_len:
                if left[curr_left] < right[curr_right]:
                    S.append(left[curr_left])
                    curr_left += 1
                else: 
                    S.append(right[curr_right])
                    curr_right += 1
            if curr_left == left_len:
                return S + right[curr_right:]
            else:
                return S + left[curr_left:]
            
        return mergeSort(nums)
            
                    
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ------------(wrong) trying to use Divide and Conquerer, but fail-------------------
#         lo, hi = 0, None
        
#         def sorting_helper(nums, lo, hi):
            
#             # Base case: only one number, no need to switch place
#             if lo == hi or nums[lo] ==nums[hi]:
#                 pass
            
                
#             # If not the same lo and hi, call recursion -> divide and conquer:
#             else:
#                 mid = (hi - lo)//2 + lo
#                 lo_val = sorting_helper(nums[lo : mid+1], lo, mid)
#                 hi_val = sorting_helper(nums[mid + 1: hi+1], mid +1, hi)
            
#                 if lo_val > hi_val:
#                     nums[lo], nums[hi] = nums[hi], nums[lo] 

            
#         return sorting_helper(nums, lo, len(nums)-1)
            
