# 1773. Count Items Matching a Rule
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        
        for i in range(len(items)):
            for j in range(len(items[i])):
                
                
                if ruleKey == "type":
                    # print('type')
                    if j == 0 and items[i][0] == ruleValue:
                        count +=1
                        # print(items[i][0])
                        # print(count)
                    else:
                        pass
                
                elif ruleKey == "color":
                    
                    if j == 1 and items[i][1] == ruleValue:
                        # print(i, j)
                        # print(items[i][1])
                        count +=1
                        # print(count)
                    else:
                        pass
                
                elif j == 2 and ruleKey == "name":
                    # print('name')
                    if items[i][2] == ruleValue:
                        count +=1
                        # print(count)
                    else:
                        pass
        return count
                    
                        
