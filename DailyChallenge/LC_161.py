# 161. One Edit Distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
     
        ns, nt = len(s), len(t)
        
        # Make sure s is always the shortest string
        if nt < ns:
            return self.isOneEditDistance(t, s)
        
        # Read through the shortest string (aka s)
        for i in range(ns):
            if s[i] != t[i]:
                
                # Case 1: ns = nt (eg: "abccd"; "acccd"-> check the string after the difference)
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                # Case 2: ns < nt; - s = "abfd", t = "acbfd"
                if nt > ns:
                    return s[i:] == t[i+1:]
                
        # Case 3: - nt-ns == 1 s = "abc", t = "abcd"
        return nt - ns == 1
    
# Time: O(n)
# Space: O(n)

            
        

    
    
    
    
#         ns, nt = len(s), len(t)
        
#         # Ensure that  s is shorter than t
#         if ns > nt:
#             return self.isOneEditDistance(t, s)
        
#         # The strings are NOT one edit away distance
#         # if the length diff is more than 1
#         if nt - ns > 1:
#             return False
        
        
#         for i in range(ns):
#             if s[i] != t[i]:
                
#                 # if strings have the same length
#                 # check rest of the string ( start with i + 1) to see if rest of the string equals after difference happens on i
#                 if ns == nt:
#                     return s[i + 1:] == t[i + 1:]
                
#                 # if strings have different lengths
#                 # t is always longer than s
#                 else:
#                     return s[i:] == t[i + 1:]
                
                
#         # If there is no diffs on ns distance
#         # the strings are one edit away only if
#         # t has one more character
#         return ns + 1 == nt
        
