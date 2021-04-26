# 1600. Throne Inheritance

class ThroneInheritance:
    
    # Step 1: Initialize the nation, king's name, and dead_list
    # Mistake: def __init(self, kingName: str):
    def __init__(self, kingName:str):
        
        # self.nation = defaultdict(list)
        # self.kingName = kingName
        # self.dead_list = set()
        
        self.nation = defaultdict(list)
        self.kingName = kingName
        self.dead_list = set()
        
    # Step 2: When there's a new born, we record its parent and its name
    def birth(self, parentName, childName):
        self.nation[parentName].append(childName)
     
    # Step 3: If there's a deadth, just add the name to the dead_list
    def death(self, name):
        # Mistake: self.dead_list.append(name)
        self.dead_list.add(name)
    
#     def getInheritanceOrder(self):
#         self. res = []
#         self.dfs(self.kingName)
#         return self.res
        
#     def dfs(self, person):
        
#         if person not in self.dead_list:
#             self.res.append(person)
        
#         for child in self.nation[person]:
#             self.dfs(child)

    def getInheritanceOrder(self):
        self. res = []
        
        def dfs(person):
        
            if person not in self.dead_list:
                self.res.append(person)

            for child in self.nation[person]:
                # Mistake: self.dfs(child); self inicates within class ThroneInheritance
                dfs(child)
            
        dfs(self.kingName)
        return self.res
        
    
            
            
        
#         res = []
        
#         # Step 4: use dfs to search each member, starting from the king
#         def dfs(person):
#             nonlocal res
#             # if king is not dead -> append the name to the result
#             if person not in dead_list:
#                 self.res.append(person)
            
#             # search through each child and children's children... using recursion
#             for child in self.nation[person]:
#                 self.dfs(child)
        
#         dfs(kingName)
        
#         return res
            
    
    
    
    
    
    
    
    
    
    
    
#     # ----------------Hash map 2 
#     def __init__(self, kingName: str):
#         # defaultdict(list) -> generate all default values with an empty list []
#         self.nation = defaultdict(list)
#         self.king = kingName
#         self.dead = set()
        
#     def birth(self, parentName: str, childName: str) -> None:
#         # nation = {parentName:[childNames, ...]}
#         self.nation[parentName].append(childName)
    
#     def death(self, name: str) -> None:
#         # dead = {dead_names, ...}
#         self.dead.add(name)
        
#     def getInheritanceOrder(self) -> List[str]:
        
#         # Initialize the ans list with an empty list
#         self.ans = []
        
#         # Starting from king 
#         self.dfs(self.king)
#         return self.ans
    
#     def dfs(self, cur):
        
#         # if kind is alive: we add his/her name to the answer
#         # else: we don't do anything -> just keep checking the children
#         if cur not in self.dead:
#             self.ans.append(cur)
        
#         for child in self.nation[cur]:
#             self.dfs(child)






# ----------------Hash map 1 and Tree
# class Node:
#     def __init__(self, name):
#         # node has two attributes: name and children []
        
#         self.name = name
#         self.children = []
        
#     def add_children(self, name):
#         # 1. Initialize a new node for a new child
#         node = Node(name) 
#         # 2. Put the name of child into children list[]
#         self.children.append(node)
#         # 3. return child node 
#         return node

# class ThroneInheritance:

#     def __init__(self, kingName: str):
#         # 1. Initialize root with kingName
#         self.root  = Node(kingName)
        
#         # 2. Initialize dead with a set
#         self.dead = set()
        
#         # 3. Use a dictionary to lookup
#         self.lookup = dict()
#         # - {kingName: root}
#         self.lookup[kingName] = self.root
       
#     def birth(self, parentName: str, childName: str) -> None:
#         # - lookup[parentName] is self.root, a node
#         # - lookup[parentName].add_children is children list[]
#         # - {childName: child node}
        
#         # lookup[childName]: add new born to the loopup
#         self.lookup[childName] = self.lookup[parentName].add_children(childName)

#     def death(self, name: str) -> None:
#         # add new deadth to dead set
#         self.dead.add(name)

#     def getInheritanceOrder(self) -> List[str]:
#         results = []
        
#         def dfs(x):
#             nonlocal results
            
#             # As long as the person is not dead, we append it to the result
#             if x.name not in self.dead:
#                 results.append(x.name)
            
#             # Traverse through to search all children for each children
#             for y in x.children:
#                 dfs(y)
        
#         dfs(self.root)
#         return results


# # Your ThroneInheritance object will be instantiated and called as such:
# # obj = ThroneInheritance(kingName)
# # obj.birth(parentName,childName)
# # obj.death(name)
# # param_3 = obj.getInheritanceOrder()
