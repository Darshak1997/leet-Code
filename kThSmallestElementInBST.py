# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        self.dfs(root, stack)
        heapq._heapify_max(stack)
        temp = heapq.nsmallest(k, stack)
        return(temp[-1])
    
    def dfs(self, root, stack):
        if root:
            stack.append(root.val)
            self.dfs(root.left, stack)
            self.dfs(root.right, stack)
