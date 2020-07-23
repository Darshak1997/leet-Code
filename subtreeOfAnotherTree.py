# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isCompare(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isCompare(self, s, t):
        if (s is not None and t is None) or (s is None and t is not None):
            return False
        elif (s is None and t is None):
            return True
        if s.val == t.val:
            if self.isCompare(s.left, t.left) and self.isCompare(s.right, t.right):
                return True
            else:
                return False
            
