# 370. Range Addition

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
#         # Naive /brute force approach: time: O(n*k); space: O(1) (if don't considered the return array)
#         returnArr = [0] * length
        
#         for update in updates:
#             for i in range(update[0], update[1]+1, 1):
#                 returnArr[i] += update[2]
#                 # print(returnArr)
#         return returnArr

        
        resArr = [0] * length
        sumAcc = 0
        
        # 1. increment for startInd (with + increment)
        # 2. Decrement for endInd + 1 (with - increment) (unless endInd is the last number in the arry)
        
        for update in updates:
            start = update[0]
            end = update[1]
            increment = update[2]
            
            resArr[start] += increment
            
            # check if the endInx is the not last number in the array (then we need to decrease the increment for endInd + 1 element)
            if (end < length - 1):
                resArr[end + 1] -= increment
                
    
        # sumAcc make resArr[i] = the sum of all numbers before curr resArr[i] + curr resArr[i]
        
        for i in range(len(resArr)):
            resArr[i] += sumAcc
            sumAcc = resArr[i]
            
        return resArr
            
            
            
            
            
            
            
            
            
            
            
            
    
