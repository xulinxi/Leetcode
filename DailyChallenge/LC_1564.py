# 1564. Put Boxes Into the Warehouse I

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        count = 0
        
        # Traverse through the warehouse:
        # Preprocess the height of the warehouse rooms to get useable heights
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
            
        # Iterate through boxes from the smallest to the larget
        boxes.sort()
        
        for room in reversed(warehouse):
            # *** Count the boxes that can fits in the current warehuose room
            # 1. count must be less than the number of the boxes we have
            # 2. Start with the first box (the smallest box) after sorting
            
            if count < len(boxes) and boxes[count] <= room:
                count += 1
                
        return count
            
        
        
