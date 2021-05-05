# # Note: we are going to use defaultdict(no keyError because has a default key value) for this problem. 
#     One example of defaultdict with set:
#         from collections import defaultdict

#         defaultdict_demo = defaultdict(set)

#         defaultdict_demo['one'].add(1)
#         defaultdict_demo['two'].add(2)
#         defaultdict_demo['one'].add('1')
#         defaultdict_demo['three']
        
#         -> return:
        
#         {'three': set(), 'two': {2}, 'one': {1, '1'}}

# print(dict(defaultdict_demo.items()))

class WordFilter:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        
        # weights dictionary contains each word and its index; e.x. {"apple":0}
        self.weights = {}
        
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            
            for char in list(word):
                prefix += char
                
                self.prefixes[prefix].add(word)
                # print(self.prefixes)
            for char in list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
                # print(self.suffixes)
            self.weights[word] = index
            # print(self.weights)
        

    def f(self, prefix: str, suffix: str) -> int:
        weight = -1
        
        # Note: and is a Logical AND that returns True if both the operands are true whereas '&' is a bitwise operator in Python that acts on bits and performs bit by bit operation. Note: When an integer value is 0, it is considered as False otherwise True when using logically.

            
        # print("****a", self.prefixes['a'] ) 
        # # -> **** 
        # print("****e", self.suffixes['e'] ) 
        
        # print("****", self.prefixes['a'] & self.suffixes['e'])  
        # -> {'appe', 'apple'} # Note: Find the common words
        # print("****", "apple" in self.prefixes[prefix] & self.suffixes[suffix]  )
        # -> True
        
        # Note: self.prefixes[prefix] & self.suffixes[suffix] -> returns a set with the common words in both self.prefixes[prefix] & self.suffixes[suffix]
        # -> then we check what word(s) satisfies are in both list (aka contains both prefixes and the suffixes)
        
        # -> We traverse through all available words and find the one with the highest weight!
        
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
