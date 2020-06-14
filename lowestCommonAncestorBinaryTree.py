# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Initialize the stack
        stack = [root]
        # Record the parent of p and q
        parent = {root: None}
        # Start iterating through the tree
        while p not in parent or q not in parent:
            node = stack.pop()
            # Iterate the left side
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            #Iterate through the right side
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        ancestors = set()
            
        while p:
            ancestors.add(p)
            p = parent[p]
            
        while q not in ancestors:
            q = parent[q]
            
        return q
        
