mp = {}
class Solution:
    
    def buildTreeUtil(self,preorder,inorder,start_index,end_index,preindex):

        global mp
        if start_index > end_index:
            return None
        val = preorder[preindex[0]]
        preindex[0] += 1
        new = TreeNode(val)
        if start_index == end_index:
            return new
        inindex = mp[val]

        new.left = self.buildTreeUtil(preorder,inorder,start_index,inindex-1,preindex)
        new.right = self.buildTreeUtil(preorder,inorder,inindex+1,end_index,preindex)
        return new

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder[0] == -1:
            return TreeNode(-1)
        global mp
        preindex=[0]

        for i in range(len(inorder)):
            mp[inorder[i]] = i
        
        root = self.buildTreeUtil(preorder,inorder,0,len(inorder)-1,preindex)
        return root