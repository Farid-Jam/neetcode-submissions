"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        nodeToClone = {}

        queue = deque([node])
        
        while queue:
            n = queue.popleft()
            if n not in nodeToClone:
                nodeToClone[n] = Node(val=n.val)
            for neigh in n.neighbors:
                if neigh not in nodeToClone:
                    nodeToClone[neigh] = Node(val=neigh.val)
                    queue.append(neigh)
                nodeToClone[n].neighbors.append(nodeToClone[neigh])
        
        return nodeToClone[node]
                    