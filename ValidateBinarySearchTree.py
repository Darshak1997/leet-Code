# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)
    
    def validate(self, root, child_max, child_min):
        if root == None:
            return True
        elif (child_max != None and root.val>=child_max) or (child_min != None and root.val<=child_min):
            return False
        else:
            return self.validate(root.left, root.val, child_min) and self.validate(root.right, child_max, root.val)
