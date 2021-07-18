# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # (Bit Manipulation) time: O(n); space: O(n) ---- jeffwei
        count = [0]
        
        for i in range(1, n+1):
            count.append(count[i>>1] + i%2)
        return count
