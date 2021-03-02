# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_s = ""
        word2_s = ""
        
        for stringx in word1:
            word1_s = word1_s + stringx
        
        for stringy in word2:
            word2_s = word2_s + stringy
            
        return word1_s == word2_s
        
