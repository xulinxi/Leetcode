# 323. Number of Connected Components in an Undirected Graph

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # --------------------Union Find
        parent = list(range(n))
        # print(parent)
        
        def find(x):
            
            # parent[x] => the connection nodes x has
            # if parent[x] != x => not a self loop or end node => connects to a different node
            if parent[x] != x:
                # Note: if 2 and 3 both connect to 1; when [1, 3] comes later, 3 will be updated as the linked node to 1, instead of 2
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry 
        
        for x, y in edges:
            union(x, y)
            
        # Note: find(i) will only return onces if there's 1 graph because find function will keep calling itself until there's no more connected nodes
        return len({find(i) for i in range(n)})
        
        
        
        
        
        
#         # -------------dfs search
        
#         def dfs(node, g, visited):
            
#             # visited[node] = 0 -> False; = 1 -> True
#             if visited[node]:
#                 return
            
#             # if visited[node] = 0 (haven't been visited)  => change it to 1 since we are currently visiting it
#             visited[node] = 1
            
#             # For each connection of the node we are at now, we run a dfs on each connection of the current node
#             for x in g[node]:
#                 dfs(x, g, visited)
                
                
#         # *** Step 1: Create a dictionary with each node and its connected node(s)
#         visited = [0] * n
#         g = {x:[] for x in range(n)}
#         for x, y in edges:
#             g[x].append(y)
#             g[y].append(x)
            
#         solution = 0
#         for i in range(n):
            
#             # Note: Since all connection will be taken care of and visited (status will be 1 in visted list), if we haven't visited this node, it means we have a new graph -> solution += 1
#             # print(visited[i]) -> 0
#             # print(not visited[i]) -> True
#             if not visited[i]:
#                 dfs(i, g, visited)
#                 solution += 1
                
#         return solution
        
        
        
        
        
        
     
        
        
        
#         # ---------bfs----------

          # *** Step 1: Create a dictionary with each node and its connected node(s)
#         unvisited = {x:[] for x in range(n)}
        
#         # Append the connected nodes for each node
#         for x, y in edges:
#             unvisited[x].append(y)
#             unvisited[y].append(x)
            
#         solution = 0
        
#         for i in range(n):
#             queue = [i]
            
#             # Note: within the future  for j in queue for loop: we are looking for all connection associated with i and its connection -> deleted the nodes we visited when we found it in the unvisited list
            
#             # if i in unvisited, it means that we hasn't deleted it yet (when we start a new cycle); ELSE: we've visited it and deleted it
#             solution += 1 if i in unvisited else 0
            
#             # check every node in queue (after we add in every node's connected nodes into queue)
#             for j in queue:
#                 # if current node is in unvisited list -> means this node was not unvisited dictionary before -> we can delete this node in visited dictionary
#                 if j in unvisited:
#                     # append the node's connected nodes to the queue, so in the next/future for loop, we can search for the connected nodes' connected nodes
#                     queue += unvisited[j]
#                     # we delete the node we've visited in the dictionary
#                     del unvisited[j]

#         return solution
    
    
    
