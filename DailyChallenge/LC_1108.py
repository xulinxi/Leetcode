# 1108. Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
#         Note: Since strings in Python are immutable, we always need to create a new string (refrain ourselves from changing them in place)
        
        result = ""

        for char in address:

            if char == ".": 
                result = result + "[" + char + "]"
            else: 
                result = result + char
        return result
        
        
        
            
        
