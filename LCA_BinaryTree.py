# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Iterative Solution
        stack = [root]
        
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
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
        
            
        
        # Recursive Solution
        # TC: O(n) and SC: O(n) 
#         self.dfs(root, p, q)
#         return self.result
    
#     def dfs(self, root, p, q):
#         if not root:
#             return False
#         left = self.dfs(root.left, p, q)
#         right = self.dfs(root.right, p, q)
        
#         # If the current node is p or q
#         mid = root == p or root == q
        
#         # If any two of the three Flags left, right, mid becomes True
#         if mid + left + right >= 2:
#             self.result = root
        
#         return mid or left or right
    
        
