# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root,], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return res
#         stack = []
#         self.dfs(root, stack)
#         return stack
    
#     def dfs(self, root, stack):
#         if root:
#             stack.append(root.val)
#             self.dfs(root.left, stack)
#             self.dfs(root.right, stack)
        
            
