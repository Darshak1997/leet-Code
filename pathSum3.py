# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # TC: O(n) and SC: O(n)
        self.dic = {}
        self.count = 0
        self.dic[0] = 1
        self.dfs(root, sum, 0)
        return(self.count)
        
    def dfs(self, root, sum, curr):
        if root:
            curr += root.val
            self.count += self.dic.get(curr - sum, 0)
            self.dic[curr] = self.dic.get(curr, 0) + 1
            self.dfs(root.left, sum, curr)
            self.dfs(root.right, sum, curr)
            # To remove the total from the dictionary during parallel processing in trees
            # No need to do this during any other data structure
            self.dic[curr] -= 1
