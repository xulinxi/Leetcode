# 953. Verifying an Alien Dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien_dict = {}
        for i in range(len(order)):
            if order[i] not in alien_dict:
                alien_dict[order[i]] = string(i)
                
        words_val = []
        word_val = ""
        for i in range(len(words)):
            words[i]
        
        
        
        
        
        
        # (Past Solution)
#         # Put order in a dictionary with an index/value to indicate the order
#         order_dict = {}
#         for i in range(len(order)):
#             order_dict[order[i]] = i
#         #     # print (order_dict)
        
#         # enumerate make a list of tuples: [(0, x0), (1, x1), (2, x2), ...]
#         # order_dict = {c:i for i,c in enumerate(order)}
        
        
#         # Loop through words; Use the order_dictionary to compare the value/order of the letters 
#         for j in range(len(words) - 1):
#             # list two words in comparison out for a clear code
#             word1 = words[j]
#             word2 = words[j + 1]
            
#             # Compare letter order first, if the letter order is corrent: compare len
#             for k in range(min(len(word1), len(word2))):
                
#                 # Make sure the first few words are not equal, if equal, check length
#                 if word1[k] != word2[k]:
#                     if order_dict[word2[k]] < order_dict[word1[k]]:
#                         print(k, order_dict[word2[k]], word2[k], order_dict[word1[k]], word1[k] )
#                         return False
#                     break
                
            
#             else:
#                 # else statement will only be executed when the if statement within for loop doesn't return. else statement is needed because it will only happen when if statement is not executed.
#                 if len(word1) > len(word2):
#                     # print(1)
#                     print(len(word1), len(word2))
#                     return False
        
#         return True
            
            
            
            
        
