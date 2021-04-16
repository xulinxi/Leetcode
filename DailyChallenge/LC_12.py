# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        
# -----------------------Approach 2: Hardcode Digits----------------------------
        

        # ------------------------Approach 1: Greedy-------------------
        
        
        digits = [ (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        
        # Loop through each symbol
        for value, symbol in digits:
            # We dont want to continue looping if we're done.
            if num == 0: break
            count, num = divmod(num, value)
            
            # Append "count" copies of "symbol" to raman_digits
                # -> if count = 0, an empty string will be appended.
            roman_digits.append(symbol * count)
            
        return "".join(roman_digits)
