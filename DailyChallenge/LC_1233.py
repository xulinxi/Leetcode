# 1233. Remove Sub-Folders from the Filesystem

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # (Wrong)
#         current_folder = folder[0]
#         res = []
#         res.append(current_folder)
#         folder_ordered = sorted(folder, key = len)
                
#         for i in range(1, len(folder_ordered)):
#             if folder_ordered[i][:len(current_folder)] == current_folder and len(folder_ordered[i]) > len(current_folder) and folder_ordered[i][len(current_folder)] == '/':
#                 continue
#             else:
#                 current_folder = folder_ordered[i]
#                 res.append(current_folder)
                
#         return res

# ----------------------------------------------------------
        # Initialize a set to store the indexes of subfolder
        sub_dictionaries = set()
        folder.sort()
        i = 0
        
        while i < len(folder):
            j = i + 1
            # if the next string in folder is a subfolder: we add the index of this string to sub_dictionaries
            while j < len(folder) and folder[i] + '/' in folder[j]:
                sub_dictionaries.add(j)
                # Moving forward to check
                j = j+1
            i = j
            
        return [each_folder for index, each_folder in enumerate(folder) if index not in sub_dictionaries]
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
            
