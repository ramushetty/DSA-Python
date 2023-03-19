class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        que = []
        que.append(root)
        res = []
        if root is None:
            return res
        while len(que)>0:

            count = len(que)
            temp=[]
            for i in range(count):
                curr_node = que.pop(0)
                temp.append(curr_node.val)
                if curr_node.left:
                    que.append(curr_node.left)
                if curr_node.right:
                    que.append(curr_node.right)
            res.append(temp)
        return res