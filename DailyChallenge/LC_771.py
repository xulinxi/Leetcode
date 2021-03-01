# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Initialize the total amount of jewels we have; we only have 0 jewel before counting
        total_jewels = 0
        jewels_dict = {}
        
        # Create a dictionary for each char in jewels
        for jewel in jewels:
            jewels_dict[jewel] = 0
            
        # Check to see if there's any stone is a jewel; keep track of the counts for each jewel stone I have
        for stone in stones:
             if stone in jewels_dict:
                    jewels_dict[stone] += 1
        
        # Add up the total number of jewel stone I have
        for jewel_type in jewels_dict:
            total_jewels = total_jewels + jewels_dict[jewel_type]
            
        return total_jewels
