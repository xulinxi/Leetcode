# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # We create a stack:
        #     - we search through the binary tree using BREADTH search
        
        # Have two queues: p_queue; q_queue:
        #         - initialize them with the first nodes, p and q, in each stack
        #         - compare the values of them by popping them:
        #             - equal: get the left node values of p and q to compare
        #                 -> equal: compare the right node 
        #                     -> equal: (starting) AND set the root to left node
        #                     -> no equal: return false
        #             - not equal:return false
            
# Note: (Using list as queue, maybe can try to use queue() in python next time.)            
        
    
    # *** Check for the empty tree (I missed this part)
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
    
    # Once we know that we have two non-empty trees: check them
        p_queue = [p]
        q_queue = [q]
        print(p_queue, q_queue)
        
        while (len(p_queue) != 0  and len(q_queue) != 0):
            node_p = p_queue.pop(0)
            node_q = q_queue.pop(0)
            
            # (check left) if the node is equal:
            #     there is a left node in both tree: add them and compare the queue
            #     there is no left nod in both tree: check right node
            if node_p.val != node_q.val:
                return False
                
            if node_p.left != None and node_q.left != None:
                    p_queue.append(node_p.left)
                    q_queue.append(node_q.left)
                    
            # If one has a left node, another one don't
            elif node_p.left != None or node_q.left != None:
                return False
            
            # (check right)
            if node_p.right != None and node_q.right != None:
                p_queue.append(node_p.right)
                q_queue.append(node_q.right)
                
            elif node_p.right != None or node_q.right != None:
                return False
        
        return True
                
            
            
# TODO: Recursive method
            
            
            
            
            
            
            
            
                    
                
        
        
        
