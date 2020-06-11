# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            # print("///Root///: ", root, "+++Stack+++: ", stack, "---Res---: ", res)
        return res[::-1]
                
            
        
        
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             self.dfs(root.right, res)
#             res.append(root.val)
    
    
