# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary = {1:"I", 4:"IV", 5:"V", 9:"IX",
        #               10:"X", 40:"XL", 50:"L", 90:"XC",
        #               100:"C", 400:"CD", 500:"D", 900:"CM",
        #               1000:"M"}
        

        # dictionary = {1:"I", 5:"V", 
        #               10:"X", 50:"L",
        #               100:"C",500:"D",
        #               1000:"M"}
        
        dictionary = {"I":1, "V":5, 
                      "X":10, "L":50,
                      "C":100, "D":500,
                      "M":1000}
        res = 0
        prev = 0
        
        for i in s:
            # find current Roman number in dictionary 
            curr = dictionary[i]
            if curr > prev:
                res += curr - 2 * prev
            else:
                res += curr
            prev = curr
        
        return res
            
            
            
            
            
            
            
            
            
            
            
            
            
        
