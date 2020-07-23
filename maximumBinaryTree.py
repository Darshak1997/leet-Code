# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.recurr(nums)
        
    def recurr(self, nums):
        if nums is None:
            return None
        curr = max(nums)
        curr_index = nums.index(curr)
        res_tree = TreeNode(curr)
        if len(nums[:curr_index]):
            res_tree.left = self.recurr(nums[:curr_index])
        if len(nums[curr_index+1:]):
            res_tree.right = self.recurr(nums[curr_index + 1:])
        return res_tree
