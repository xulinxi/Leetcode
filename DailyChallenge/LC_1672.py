# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
#         To keep track of the richest person, we need to keep track of who's the richest person so far.
        max = 0
        
        for i in range(len(accounts)):
#             Starting with 0, find out how much each person has
            current_max = 0
            for j in range(len(accounts[i])):
                current_max = current_max + accounts[i][j]
            if current_max > max:
                max = current_max
                
        return max
                
            
            
