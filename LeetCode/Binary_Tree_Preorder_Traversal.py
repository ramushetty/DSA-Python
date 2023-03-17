class Solution:
    def preorderTraversalUtil(self,root,res):
        if root is None:
            return
        res.append(root.val)
        self.preorderTraversalUtil(root.left,res)
        self.preorderTraversalUtil(root.right,res)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        self.preorderTraversalUtil(root,res)
        return res