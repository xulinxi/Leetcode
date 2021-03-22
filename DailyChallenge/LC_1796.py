# 1796. Second Largest Digit in a String

class Solution:
    def secondHighest(self, s: str) -> int:
        
        # digit_list = []
        # for i in s:
        #     if i.isdigit():
        #         digit_list.append(int(i))
        # OR
        digit_set = {int(i) for i in s if i.isdigit()}
        print (digit_set)
         
#         if len(digit_set) == 0:
#             return -1
        
        # Check if the length == 1:
        if len(digit_set) < 2:
            return -1
        
#         else:
#             # Check if all items are the same:
#             first_dig = list(digit_set)[0]
#             check_same = False
#             for each in digit_list:
#                 if each != first_dig:
#                     check_same = False
#                     break
#                 else:
#                     check_same = True
#             if check_same:
#                 return -1
            
        else:
            # print(digit_list)
            largest = float('-inf')
            second_largest = float('-inf') - 1

            # Sorting can be used.
            # OR delete the largest num, the largest num remain will be the second largest num
            for digit in list(digit_set):
                if digit > largest:
                    largest = digit
            digit_set.remove(largest)

            for digit in list(digit_set):
                if digit > second_largest:
                    second_largest = digit

            return second_largest

                
