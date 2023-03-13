def getMaxWidth(self,root):
       
        #code here
        
        que = []
        que.append(root)
        res = 0
        while len(que) > 0:
            count = len(que)
            res = max(res,count)
            for i in range(count):
                curr_node = que.pop(0)
                if curr_node.left is not None:
                    que.append(curr_node.left)
                if curr_node.right is not None:
                    que.append(curr_node.right)
        return res