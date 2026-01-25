import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, current_max):
            if root:
                if root.val >= current_max:
                    self.res += 1

                current_max = max(current_max, root.val)
                dfs(root.left, current_max)
                dfs(root.right, current_max)

        dfs(root, -sys.maxsize-1)
        return self.res
