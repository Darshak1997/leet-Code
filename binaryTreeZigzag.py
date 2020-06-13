# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        level = 0
        if not root:
            return []
        
        queue = deque([root,])
        
        while queue:
            levels.append([])
            levelLength = len(queue)
            for i in range(levelLength):
                node = queue.popleft()
                
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level%2 == 1: 
                levels[level] = levels[level][::-1]
            level += 1
        return levels
        
