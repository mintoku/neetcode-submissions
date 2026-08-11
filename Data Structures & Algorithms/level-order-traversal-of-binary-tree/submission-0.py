# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        if not root:
            return []
        res = []
        while q:
            lenQ = len(q)
            level = []
            for i in range(lenQ):
                level.append(q[i].val)
            res.append(level)
            for i in range(lenQ):
                node = q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res