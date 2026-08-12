# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # O(n) DFS recursive
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), 
        # self.maxDepth(root.right))

        # BFS iterative
        # if not root: 
        #     return 0

        # queue = collections.deque([root])
        # depth = 0

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     depth += 1
        
        # return depth

        # DFS iterative
        if not root:
            return 0
        
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(depth, result)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return result
