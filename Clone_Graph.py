#Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
#Output: [[2,4],[1,3],[2,4],[1,3]]
#Explanation: There are 4 nodes in the graph.
#1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
#2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
#3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
#4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone = Node(node.val, [])
        self.visited[node] = clone
        
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone
