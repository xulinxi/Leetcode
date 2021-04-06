# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        best = 0
        current = 0
        
        # looking for first three cards' sum from the front
        for x in range(k):
            current += cardPoints[x]
            
        best = max(best, current)
        
        N = len(cardPoints)
        for x in range(k):
            current -= cardPoints[k-x-1]
            current += cardPoints[N-x-1]
            best = max(best, current)
            
        return best
