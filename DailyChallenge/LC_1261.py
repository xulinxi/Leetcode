# 1261. Find Elements in a Contaminated Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        # Mistake: def recover(self, root: TreeNode): 
        # Any function defined within a scope can use variables from its enclosing scope. In this case, you're defining a function within a function, so all the variables in the enclosing function are available - self, param1, and param2. So you can pass self as a parameter to the inner function, but since it already has access to self, there's not much point to doing so.

# If you create new variables with these names inside your new function, they "shadow" the variables with those names in the outer scope, meaning the names from the outer scope are inaccessible as long as the same names refer to something else in the inner scope. self is just a normal variable name with no special meaning, except that it's the first parameter of a class's instance function, and thus gets passed implicitly when the method is called via the dot operator - meaning that it's subject to these rules. 

        def recover(root):
            if root:
                self.val_set.add(root.val)
                if root.left:
                    root.left.val = 2 * root.val + 1
                    recover(root.left)
                if root.right:
                    root.right.val = 2 * root.val + 2
                    recover(root.right)
            else:
                return
            
        root.val = 0
        self.val_set = set()
        recover(root)
            

    def find(self, target: int) -> bool:
        return target in self.val_set
    
    
    
    
    
    # ----------------------------------------------------(HashMap)
#     def __init__(self, root: TreeNode):
#         def recover(node):
#             if not node:
#                 return
#             self.values.add(node.val)
            
#             if node.left:
#                 node.left.val = 2 * node.val + 1
#                 recover(node.left)
#             if node.right:
#                 node.right.val = 2 * node.val + 2
#                 recover(node.right)
                
#         # Use a set to memorize all node vals generated for find function
#         self.values = set()
#         # Reset root val = 0
#         root.val = 0
#         recover(root)
        
#     def find(self, target: int) -> bool:
#         return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
