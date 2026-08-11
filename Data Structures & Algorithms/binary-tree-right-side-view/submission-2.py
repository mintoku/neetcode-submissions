# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        q.append(root)
        while q:
            lenQ = len(q)
            if lenQ == 1 and q[0]:
                res.append(q[0].val)
            if lenQ > 1:
                res.append(q[-1].val)
                
            for i in range(lenQ):
                node = q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return res


            