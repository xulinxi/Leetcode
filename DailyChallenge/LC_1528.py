# 1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        result_list = [None] * len(s)
        result_string = ""
        
        for i in range(len(indices)):
            result_list[indices[i]] = s[i]
            # print(index, result_list)
            
        for char in result_list:
            result_string += char
            
        return result_string
        
