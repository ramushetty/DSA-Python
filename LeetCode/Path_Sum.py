class Solution:

    def pathsum(self,root,targetSum):
        if root is None:
            return False

        if root.left is None and root.right is None and targetSum-root.val == 0:
            return True
        if self.pathsum(root.left,targetSum-root.val) or self.pathsum(root.right,targetSum-root.val):
            return True
        return False
        


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathsum(root,targetSum)