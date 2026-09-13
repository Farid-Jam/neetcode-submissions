# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((0, root))
        res = []

        while queue:
            level, node = queue.popleft()

            if node:
                if len(res) == level:
                    res.append([node.val])
                else:
                    res[level].append(node.val)
                
                queue.append((level + 1, node.left))
                queue.append((level + 1, node.right))

        return res
