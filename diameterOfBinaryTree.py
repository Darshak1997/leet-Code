# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        self.dfs(root)
        return self.ans - 1
    
    def dfs(self, root):
        if root:
            # print("Root*****:", root)
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            # print("Left****:", left)
            # print("Right***:", right)
            self.ans = max(self.ans, left+right+1)
            # print("Answer***:", self.ans)
            # print("Returned***: ", max(left, right)+1)
            return max(left, right) + 1
        # print("None Output")
        return 0
