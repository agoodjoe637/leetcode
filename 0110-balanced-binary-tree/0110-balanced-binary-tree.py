
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def whatsDepth(root):
            if not root:
                return 0
            
            left_depth = whatsDepth(root.left)
            if left_depth == -1: return -1
            right_depth = whatsDepth(root.right)
            if right_depth == -1: return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1 
            
            return 1 + max(left_depth,right_depth)
        
            
        return whatsDepth(root) != -1 