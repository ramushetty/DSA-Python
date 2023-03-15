class Solution:
    def inordertraversalutil(self, root,res):
        if root is None:
            return None
        
        self.inordertraversalutil(root.left,res)
        res.append(root.val)
        self.inordertraversalutil(root.right,res)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.inordertraversalutil(root,l)
        return l