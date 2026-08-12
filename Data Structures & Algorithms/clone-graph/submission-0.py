"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.old_to_new = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
     
        if node in self.old_to_new: #already made a clone
            return self.old_to_new[node] #return new node
        
        copy = Node(node.val, [])
        self.old_to_new[node] = copy #map old to copy

        #make copies of every neighbor
        for neighbor in node.neighbors:
            copy.neighbors.append(self.cloneGraph(neighbor))
        
        return copy