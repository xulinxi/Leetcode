# 278. First Bad Version


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Mistake: low = 0 version starts with 1
        low = 1
        
        # Note: need to put n//2 within while loop -> keep updating until base case happens
        # mid = n //2
        high = n
        
        # ***Make sure sure while loop to keep checking
        while low < high:
            mid = (low + high) // 2
            # if mid is a bad version, we need to check the version before mid
            if isBadVersion(mid):
                high = mid
            
            # *** if mid is not true, this means the bad version appears later (in later range)
            else:
                # Mistake: low = mid -> Mid has been checked
                low = mid + 1
                
        return low
            
        
        
        
        
        # Time Limit Exceeded --------------------

        # for i in range(n+1):
        #     if isBadVersion(i):
        #         return i
            

        
