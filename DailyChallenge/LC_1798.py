# 1798. Maximum Number of Consecutive Values You Can Make

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        # TODO: rewrite sort
        res = 1
        
        for i in sorted(coins):
            if res < i:
            # if res > i:
                break
            res = res+i
            
        return res
    
    # -------_Ref answers:
        # def getMaximumConsecutive(self, A):
        # res = 1
        # for a in sorted(A):
        #     if a > res: break
        #     res += a
        # return res
        
