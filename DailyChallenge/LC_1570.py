# 1570. Dot Product of Two Sparse Vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums
        
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        # (Iterative Way)
          # result = 0
#         Iterate through nums1 
        
#         nums1 = [1,0,0,2,3]
#         nums1[i]
#         nums2 = [0,3,0,4,0]
#         nums2[i]
        
        # i = 0                           1           ....
        # nums1[0] * nums2[0]  +  nums1[1] * nums2[1] + ...
        
        # time: O(n); space: O(1)
        
        # Initialize result
        result = 0  # result = 6
        
        # Iterate through each element in matching index (nums and vec)
        for i in range(len(self.array)):    # 0 - 6; 0
            result += self.array[i] * vec.array[i] 
            
            # result += self.array[1] * self.vec.array[1] = 0 + 0 + ... 2*3 + 0 = 6
            
        return result
        
        # nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
        
        # time: O(n); space: O(1)
        
        # (Hash Map)
#         nums1 = [1,0,0,2,3]
#         nums1_dict = {0: 1, 3: 2, 4: 3}
        
#         nums2 = [0,3,0,4,0]            
#         nums2_dict = {1: 3, 3: 4}
        
#         result = 0
        
        # while loop (iterate through the dict1 -> check if there's a matching index in dict2) 
        
        # time: O(n); space: O(2n = n)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ---- Mine
        
    # def __init__(self, nums: List[int]):
    #     self.array = nums
    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     result = 0
    #     for i in range(len(self.array)):
    #         # result += self.array[i] * vec[i]
    #         result += self.array[i] * vec.array[i]
    #     return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# My understanding: v1.dotProduct(v2) -> v1 is initilalized by __init__ function and v2 is vec in dotProduct
