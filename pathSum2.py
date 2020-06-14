# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.add(root, sum, [], res)
        return res
    
    def add(self, root, sum, path, res):
        if root:
            if not root.left and not root.right and root.val == sum:
                res.append(path+[root.val])
            self.add(root.left, sum-root.val, path+[root.val], res) 
            self.add(root.right, sum-root.val, path+[root.val], res)
