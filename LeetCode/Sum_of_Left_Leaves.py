class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def SumLeft(root,isLeft):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                if isLeft:
                    return root.val
                else:
                    return 0
            return SumLeft(root.left,True) + SumLeft(root.right,False)
        return SumLeft(root,False)