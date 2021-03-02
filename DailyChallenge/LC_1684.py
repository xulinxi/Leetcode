# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
#         create a dictionary with characters in allowed
            allow_set = set()
    
            for letter in allowed:
                allow_set.add(letter)

            count = 0

            for chars in range(len(words)):
                for char in words[chars]:
                    if char not in allow_set:
                        count +=1
                        break
            return len(words) - count
                
                
                    
                    
            
        
