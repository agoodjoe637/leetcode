from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def maxDepth(root):
            if not root:
                return 0
            left_depth = maxDepth(root.left)
            right_depth= maxDepth(root.right)

            self.max_diameter = max(
                self.max_diameter, left_depth + right_depth
            )
            return 1 + max(left_depth, right_depth)

        maxDepth(root)

        return self.max_diameter
