# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dx, px, dy, py = self.dfs(root, None, 0, x) + self.dfs(root, None, 0, y)
        return dx == dy and px != py
        
    def dfs(self, node, parent, depth, mod):
        if node:
            if node.val == mod:
                return depth, parent
            return self.dfs(node.left, node, depth+1, mod)or self.dfs(node.right, node, depth+1, mod)
            
