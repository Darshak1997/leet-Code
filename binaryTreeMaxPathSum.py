# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPath = -inf
        self.helper(root)
        return self.maxPath
        
        
    def helper(self, root):
        if root:
            leftSum = max(self.helper(root.left), 0)
            rightSum = max(self.helper(root.right), 0)
            currPathSum = root.val + leftSum + rightSum
            self.maxPath = max(self.maxPath, currPathSum)
            return root.val + max(leftSum, rightSum)
        return 0
            
