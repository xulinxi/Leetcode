# 744. Find Smallest Letter Greater Than Target


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        
        
        
        
        
        
        # ---- Mine (Wrong) + rhyang (Correction)
#         if target == 'z':
#             return letters[0]
        
        # else:
        low, high = 0, len(letters) - 1
        # BUG: mid = (low + high) // 2
        # print(low, high)
        result = 0
            
        while low <= high:
            mid = (low + high) // 2
            # if letters[mid] == target:
            #     return letters[mid + 1]
            # elif ord(letters[mid]) < ord(target):
            #     low, high = mid + 1, high
            # else:
            #     low, high = low, mid - 1

            if letters[mid] > target:
                result = mid
                high = mid - 1
            else: # letters[mid] <= target
                    low = mid + 1
            
        return letters[result]
                    
        # b c e f  j  k l m    *d
        
        # ["b", "c", "e", "f", "j", "k", "l", "m"]
        # "d"
