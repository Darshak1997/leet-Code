# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Root: ", root.val)
        print("P: ",  p.val)
        if root.val == p.val or root.val == q.val:
            print("1")
            print(root.val)
            return root
        elif (p.val > root.val > q.val) or (q.val > root.val > p.val):
            print("2")
            return root
        elif p.val == q.val:
            print("3")
            return None
        elif p.val < root.val and q.val < root.val:
            print("4")
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            print("5")
            return self.lowestCommonAncestor(root.right, p, q)
            
