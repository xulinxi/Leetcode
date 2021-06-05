# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
#         # Approach 1: Merge and Sort-------------------------------------
        
#         # Write the elements of nums2 into the end of nums2
#         for i in range(n):
#             nums1[i + m] = nums2[i]
            
#         # Sort nums1 list in-place.
#         nums1.sort() 
        
#         # Time: O((n+m)log(n+m))
#         # Space: O(n) -> Note: add n numbers (nums from nums2) to nums1
        
        
        
#         # Appraoch 2: Three Pointers (Start From the Beginning)-----------------
        
#         # Make a copy of the first m elements of nums1.
#         nums1_copy = nums1[:m]
        
#         # Read pointers for nums1Copy and nums2 respectively. 
        
#         # Initialize read pointer p1 to the beginning of nums1_copy
#         p1 = 0 
#         # Initialize read pointer p2 to the beginning of nums2
#         p2 = 0
        
#         # Compare elements from nums1_copy and nums2 and write the smallest to nums1.
#         for p in range(n+m):
            
#             # We also need to ensure that p1 and p2 aren't over the boundaries 
#             # of their respective arrays

#             # if no more number in nums2 (p2 >= n); end of p2
#             # OR
#             # still has number left in nums1
#             # -> (p1 < p2) if th2 nums in nums1 is smaller than the one in nums2
            
#             if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
#                 nums1[p] = nums1_copy[p1]
#                 p1 += 1
            
#             # p2 < p1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 += 1

        # Time: O(n + m)
        # Note: We are performing n + 2*m reads and n + 2*m writes. 
        # (Make a copy of nums1 with m nums)            
        # Because constants are ignored in Big O notation, this gives us a time complexity of O(n+m)
        # Space: O(m)
        # We are allocating an additional array of length m.
                
                
                
                    
        # Approach 3: Three Pointers (Start From the End)-----------------
        
        # Note: the number of trailing 0 in nums1 = size of nums2 (n)
            
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
            
        # And move p backwards through the array, each time writing
        # The smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            
            # when checked all numbers in nums2 -> break
            if p2 < 0:
                break
            
            # when still have nums in nums & nums1[p1] > nums2[p2]
            # Note: since we are traversing from the back: we are getting the most updated largest number at the end
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                
            # nums[p2] > nums1[p1]
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        
        
            
        
        
            
        
        
        
        
        
        
        
        
        
        
        
