# 169. Majority Element


# Note: There are six approaches to this problem. Make sure to finish them all.
# huahua blog has eight approaches


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        
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

# ---------------------------------------Approach 5: Divide and Conquer-----------------------------



        
        
                
        
