# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.backtrack(root, sum)
        
    def backtrack(self, root, curr):
        if root:
            if not root.left and not root.right and root.val == curr:
                return True
            return self.backtrack(root.left, curr-root.val) or self.backtrack(root.right, curr-root.val)
            
