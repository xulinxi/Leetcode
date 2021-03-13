# 297. Serialize and Deserialize Binary Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # -------------------------------Resursive Solution
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return 'x'      
        # Create an empty to store all node values with ',' as their separator
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

        
    def deserialize(self, input_data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Creating a class variable (self.data) to store input data (should be a decoded list)
        # To avoid lost of data during the recursion
        # *** Note: Keep slicing the data/ updating the rest of the data***
        self.data = input_data
        
        # (self can be ignored in this case)
        # ***Note: we can also use input_data in this case:
                # (cons) super slow: because if we use self.data -> has already stoed while input_data was not stored
        if self.data[0] == 'x':
            return None
        
        # if we have a nonempty tree: we start constructing a tree
        # .find() function finds the first ','
        # self.data[:self.data.find(',')] will return node value right before the first comma
        node = TreeNode(self.data[ : self.data.find(',') ], None, None)
        
        node.left = self.deserialize(self.data[self.data.find(',') + 1 : ])
        
        node.right = self.deserialize(self.data[self.data.find(',') + 1 : ])
        
        return node
        
        
        
# ---------------------------------------------------------------------------(Wrong answer - iterative)
#    def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """     
#         # Loop through the tree using level traversal
#         # Add in each node value or null (if no node) to a string

#         tree_string = ''
        
        
#         search_queue = []
#         search_queue.append(root)
        
#         while root: 
#             while search_queue:
#                 root = search_queue.pop(0)
#                 tree_string += str(root.val) 
#                 tree_string += ','
#                 if root.left:
#                     search_queue.append(root.left)
#                 if root.right:
#                     search_queue.append(root.right)
#                 elif not root.left:
#                     tree_string += 'null'
#                     tree_string += ','
#                 elif not root.right:
#                     tree_string += 'null'
#                     tree_string += ','
                    
#         return search_queue

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
        
#         # Split the string using ',' as the separator for the string to get each node value in order
#         # Put each node value in an array queue
#         # starting with the first value is the root
#         # Dequeue the array using breadth first traversal
        
#         tree_queue = tree_string.split(',')
        
#         while tree_queue:
#             root_val = tree_queue.pop(0)
#             if not 'null':
#                 node = TreeNode(int(root_val), None, None)
                
                
#                 # How to connect nodes together???
                
#             if 'null':
#                 # convert it back to null???

# ------------------------------------------------------------------------------------------            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
