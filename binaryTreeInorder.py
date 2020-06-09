# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right
            
        return(res)
                
            
        
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             res.append(root.val)
#             self.dfs(root.right, res)
            
