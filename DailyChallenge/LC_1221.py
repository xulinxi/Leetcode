# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # Loop through each char in the string 
        # -> initialize count = 0; if "R" + 1; if "L" -1 
        # -> initialize pair = 0; when count goes back to 0, pair + 1
        
        pair = 0
        count = 0
        
        for char in s:
            
            if char == "R":
                count += 1
                if count == 0:
                    # If balanced, increase the pair count
                    pair += 1
            elif char == "L":
                count -= 1
                if count == 0:
                    pair += 1
                    
        return pair

            
        
