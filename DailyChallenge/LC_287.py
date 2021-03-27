# 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        # ---------Hash Table method----------
#         nums_dup = {}
        
#         for num in nums:
#             if num not in nums_dup:
#                 nums_dup[num] = 1
#             else:
#                 nums_dup[num] += 1
                
#         # Note: ***syntaxs mistake: "for key, value in nums_dup":
#         for key, value in nums_dup.items():
#             if value > 1:
#                 return key
            
            
# --------Follow Up: improve time complexity to O(logn): NOT Possible----------------

# --------Follow Up: improve space complexity to O(1) (brute-force: doesn't go through when sample size > ~2000)-----------
    
        # for curr_num in range(0, len(nums)-1, 1):
        #     for next_num in range(curr_num + 1, len(nums), 1):
        #         if nums[curr_num] == nums[next_num]:
        #             return nums[curr_num]

        # ------------Follow Up: Pointer Method (TODO: understand this code)--------------------
        # Approach 3: Floyd's Tortoise and Hare (Cycle Detection) TODO: understand this method
        slow, fast, finder = 0, 0, 0
        
        while True:
            # nums[nums[nex]]: means takes an value for index
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
            
            
        
            
        
