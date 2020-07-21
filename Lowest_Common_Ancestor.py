# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val, q_val = p.val, q.val
        
        if parent_val > p_val and parent_val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif parent_val < p_val and parent_val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
