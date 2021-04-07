# 66. Plus One


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        
        
        n = len(digits)
        
        # Move along the input array starting from the end of the array
        for i in range(n):
            idx = n - 1 - i
            
            # Set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
                
            # If rightmost not-nine:
            else:
                # Increase this rightmost not-nine by 1; even in the case (ex: 189), the added 1 just move to the next place -> no need to think about carry situation
                digits[idx] += 1
                # and the job is done
                return digits
            
        # If all digits are nines  
        return [1] + digits
