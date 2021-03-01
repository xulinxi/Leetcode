# 1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        num_dict = {}
        total_pairs = 0
        
        for num in nums:
            if num in num_dict.keys():
                num_dict[num] += 1
                # print(num,num_dict[num])
              
            else:
                # print(num)
                num_dict[num] = 1
        # print(num_dict)
              
        for num_key in num_dict:
            # print(num_dict[num_key])
            each_pairs = num_dict[num_key]*(num_dict[num_key]-1)//2
            total_pairs = total_pairs + each_pairs
            
            
        return total_pairs
                
