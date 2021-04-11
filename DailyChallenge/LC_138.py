# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        
        if not head:
            return head
        
        # Creating a new weaved list of original and copied nodes.
        pointer = head
        
        while pointer:
            
            # Cloned node
            new_node = Node(pointer.val, None, None)
            
            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            # Set A'->B
            new_node.next = pointer.next
            # Set A->A'(->B)
            pointer.next = new_node
            # Move pointer to B
            pointer = new_node.next
        
        # Reset Pointer because we need to connect random nodes now (loop throught the list again)
        pointer = head
        
        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers, to assign references to random pointers for cloned nodes.
        while pointer:
            
            # pointer.next: A', pointer.next.random: trying to set the random of cloned node
            # pointer.random: the random next node of the original node A; pointer.random.next: the cloned node of A's random next node -> connect A' to the cloned random node
            pointer.next.random = pointer.random.next if pointer.random else None
            # Move the pointer to node B (aka the next node)
            pointer = pointer.next.next
            
        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        point_old_list = head # (target:)A->B->C; (current: A->A'->B->B'->C->C')
        point_new_list = head.next # (target:)A'->B'-C'(current: A'->B->B'->C->C')
        
        # Holder for new cloned list
        head_new = head.next
        
        while point_old_list:
            # if statement is not requirement because the last element availabel will be: C->C'->None (point_old_list.next always exits because original is followed by a cloned node)
            point_old_list.next = point_old_list.next.next
            
            # if statement is requirement because (ex: C'->None)
            point_new_list.next = point_new_list.next.next if point_new_list.next else None
            # Move forward
            point_old_list = point_old_list.next
            point_new_list = point_new_list.next
            
        return head_new
    
    
    
    
    
    
    
    
    
# ---------------Hash Map-------------------------------------
#     def __init__(self):
#         # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
#         self.visited = {}
    
#     def getClonedNode(self, node):
#         # If node exists then
#         if node:
#             # Check if its in the visited dictionary
#             if node in self.visited:
#                 # If its in the visited dictionary then return the new node reference from the dictionary
#                 return self.visited[node]
#             else:
#                 # Otherwise create a new node, save the reference in the visited dictionary and return it.
#                 self.visited[node] = Node(node.val, None, None)
#                 return self.visited[node]
#             return None
        
#     def copyRandomList(self, head: 'Node') -> 'Node':
        
#         if not head:
#             return head
        
#         old_node = head
        
#         # Creating the new head node
#         new_node = Node(old_node.val, None, None)
#         self.visited[old_node] = new_node
        
#         # Iterate on the linked list until all nodes are cloned.
#         while old_node != None:
            
#             # Get the clones of the nodes referenced by random and next pointers.
#             new_node.random = self.getClonedNode(old_node.random)
#             new_node.next = self.getClonedNode(old_node.next)
            
#             # Move one step ahead in the linked list.
#             old_node = old_node.next
#             new_node = new_node.next
            
#         return self.visited[head]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
