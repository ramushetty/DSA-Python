class Solution:
    def postorderTraversalUtil(self, root: Optional[TreeNode],res):
        if root is None:
            return 
        self.postorderTraversalUtil(root.left,res)
        self.postorderTraversalUtil(root.right,res)
        res.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorderTraversalUtil(root,res)
        return res