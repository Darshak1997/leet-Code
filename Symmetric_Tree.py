class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return helper(L.left, R.right) and helper(L.right, R.left)
            return False
        return helper(root, root)
