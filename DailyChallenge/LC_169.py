# 169. Majority Element

# Note: There are six approaches to this problem. Make sure to finish them all.
# huahua blog has eight approaches
# Classical approaches: Divide and Conquer, Hash map, and full sorting (median will be the majority)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
# ---------------------------------------Approach 5: Divide and Conquer (from LC) ---------
        lo = 0
        hi = None
        
        # Create a helper function that recognizes the majority number within nums list and its sublists
        def majority_rec(nums, lo, hi):
            # Step 1: check for the base case: lo = hi
            if lo == hi:
                return nums[lo]
                
            # Step 2: Resursion: devide the nums list into half and then call majority_rec for each half; create a mid index
            
            mid = (hi - lo)//2 + lo
            # ***Mistake: Make sure mid is changing while the dividing 
            # mid = len(nums) // 2 + lo
            left = majority_rec(nums, lo, mid)
            right = majority_rec(nums, mid+1, hi)
            
            if left == right:
                return left
            
            # if two sides don't have the same majority number, loop through the current list/sublist to check which number (left or right) is the majority number
            else:
                left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
                right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        
            # ****Make sure keep returning the majority while we are checking the left and right
            return left if left_count > right_count else right
                                  
        # Note: after we create the helper function, we gotta call it in the big function.
        # ***Mistake: make sure to return len(nums)-1 as the hi because hi is initialize as None***
        # return majority_rec(nums, lo, hi)
        return majority_rec(nums, lo, len(nums) -1)
    
    
    # ------------------_TODO: other methods!!!

        
        
        
    
    
    
    
    
    
    
    
    
    
    
# ---------------------------------------(My approach) Similar to Approach 2: HashMap-----------------------------
        nums_len = len(nums)
        
        nums_dic = {}
        
        for num in nums:
            if num in nums_dic:
                nums_dic[num] += 1
            else:
                nums_dic[num] = 1

        return max(nums_dic.keys(), key = nums_dic.get)
        # also can be: return max(nums_dic, key = nums_dic.get)




        
        
                
        
