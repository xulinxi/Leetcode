# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
#         Find the max_candies (O(n))
#         (If max() cannot be used) 

#       keep track of the max value
        max = 0
#       return result
        output = []
        
        for each in candies:
            if each > max:
                max = each
            else:
                pass
        
#         Compare each candies[i] + extra candies with the max_candies
        for each in candies:
            output.append(each + extraCandies >= max)

        return output
                
                
            
    
    
    
