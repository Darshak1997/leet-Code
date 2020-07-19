# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.helper(collections.deque(preorder), inorder, 0, len(preorder)-1)
    
    def helper(self, preorder, inorder, ii, ij):
        if ii > ij:
            return None
        val = preorder.popleft()
        root = TreeNode(val)
        index = self.dic[val]
        
        root.left = self.helper(preorder, inorder, ii, index - 1)
        root.right = self.helper(preorder, inorder, index + 1, ij)
        
        return root
    
        
        
            
