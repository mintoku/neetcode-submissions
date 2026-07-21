# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def height(root):
            if not root:
                return 0
            leftHeight = 1 + height(root.left)
            rightHeight = 1 + height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                self.isBalanced = False
            return max(leftHeight, rightHeight)
        height(root)
        return self.isBalanced

