# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
#         # (Dictionary) time: O(n); space: O(n) ---- Mine
#         num_dict = {}
        
#         for num in nums:
#             if num not in num_dict:
#                 num_dict[num] = 1
                
#             else:
#                 num_dict[num] += 1
                
                
#         # Note: Make sure to clarify the expected results:
#         #         My thought: all num must appear at lest twice
#         #         Correct: Any value that occurs at least twice will make this works
#         for v in num_dict.values():
#             if v > 1:
#                 return True
#         return False



#         # (Set) ---- Solution
#         # num_set = set(i for i, num in enumerate(len(nums)))
#         # num_set = set([i for i, num in enumerate(nums)])
#         # print(num_list)
#         # print(num_set)
#         num_set = set()
        
#         for num in nums:
#             if num in num_set:
#                 return True
#             num_set.add(num)
#         return False
            
    
    
    
    
