# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root) -> int:
            if not root:
                return -1
            
            height_left = 1 + dfs(root.left)
            height_right = 1 + dfs(root.right)
            self.diameter = max(self.diameter, height_left + height_right)

            return max(height_left, height_right)
        dfs(root)
        return self.diameter

