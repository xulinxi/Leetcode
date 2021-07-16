# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        output_set = set()
        
        set1 = set(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] in set1:
                output_set.add(nums2[i])
                
        return output_set
