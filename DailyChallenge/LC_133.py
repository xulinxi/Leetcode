# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        # Step 1: Initialize a dictionary to remember all visited nodes
        visited = {}
        
        
        # Step 2: Initialize a queue to remember the order we bfs through the graph
        # Mistake: queue = deque(node); deque has use with a list object
        queue = deque([node])
        
        
        # ***Remmeber to initialize the visited with the first node
        visited[node] = Node(node.val, [])
        print(visited)
        
        # While we have a node in queue, we check it's neighbor and check if we need to make a copy
        while queue:
            # Mistake curr = deque.leftpop(); deque only has popleft()
            curr = queue.popleft()
                
            # We copy the neighbors of the visited node to the cloned node
            for neighbor in curr.neighbors:
                # if we haven't visited this node before, we added to the visited with its cloned node
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    # ***append neighbot to the queue for future iteration
                    queue.append(neighbor)
                
                # Adding the cloned neighbors to list is establishing the connection
                visited[curr].neighbors.append(visited[neighbor])
      
        return visited[node]
                
    



# -------------BFS (using list as a queue): Pop: O(n)

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return node
        
#         # Dictionary to save the visited node and it's respective clone
#         # as key and value respectively. This helps to avoid cycles
#         visited = {}
        
#         # Put the first node in the queue
#         queue = [node]
#         # Clone the node and put it in the visited dictionary.
#         visited[node] = Node(node.val, [])
        
#         # Start BDF traversal
#         while queue:
#             # Pop a node say "n" from the front of the queue.
#             n = queue.pop(0)
#             # print(n)
#             # Iterate through all the neighbors of the node
#             for neighbor in n.neighbors:
#                 if neighbor not in visited:
#                     # Clone the neighbor and put in the visited, if not present already
#                     visited[neighbor] = Node(neighbor.val, [])
#                     # Add the newly encouxntered node to the queue.
#                     queue.append(neighbor)
                
#                 # Add the clone of the neighbor to the neighbors of the clone node "n"
#                 visited[n].neighbors.append(visited[neighbor])
        
#         # Return the clone of the node from visited.
#         return visited[node]
    
    
    # ----------------------BFS: Pop: O(1)
# from collections import deque

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return node
        
#         # Dictionary to save the visited node and it's respective clone
#         # as key and value respectively. This helps to avoid cycles
#         visited = {}
        
#         # Put the first node in the queue
#         queue = deque([node])
#         # Clone the node and put it in the visited dictionary.
#         visited[node] = Node(node.val, [])
        
#         # Start BDF traversal
#         while queue:
#             # Pop a node say "n" from the front of the queue.
#             n = queue.popleft()
#             # Iterate through all the neighbors of the node
#             for neighbor in n.neighbors:
#                 if neighbor not in visited:
#                     # Clone the neighbor and put in the visited, if not present already
#                     visited[neighbor] = Node(neighbor.val, [])
#                     # Add the newly encountered node to the queue.
#                     queue.append(neighbor)
                
#                 # Add the clone of the neighbor to the neighbors of the clone node "n"
#                 # visited[n] = n'
#                 # visited[n].neighbors = n's.neighbors = []; a list contains all neighbors of n'
                  # visited[neighbor] = neighbor'
#                 visited[n].neighbors.append(visited[neighbor])
        
#         # Return the clone of the node from visited.
#         return visited[node]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
