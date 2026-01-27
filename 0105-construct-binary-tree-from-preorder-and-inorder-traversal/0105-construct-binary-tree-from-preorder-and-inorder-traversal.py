class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left,right):
            if left> right:
                return None 
            
            root_val = preorder[self.pre_idx]
            root= TreeNode(root_val)
            self.pre_idx += 1

            mid = inorder_map[root_val]

            root.left =  build(left,mid-1)
            root.right =  build(mid+1,right)
            return root
        
        return build(0,len(inorder)-1)