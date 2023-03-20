# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

mp = {}

class Solution:
    def buildTreeUtil(self,inorder,postorder,start_index,end_index,preIndex):
        global mp
        if start_index > end_index:
            return None
        print(preIndex[0])
        new_node = TreeNode(postorder[preIndex[0]])
        preIndex[0] -=1
        if start_index == end_index:
            return new_node
        inIndex = mp[new_node.val]
        new_node.right = self.buildTreeUtil(inorder,postorder,inIndex+1,end_index,preIndex)
        new_node.left = self.buildTreeUtil(inorder,postorder,start_index,inIndex-1,preIndex)
    
        return new_node


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder[0] == -1:
            return TreeNode(-1)   
        global mp
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        preIndex = [len(postorder)-1]
        start_index=0
        end_index = len(inorder)-1
        res = self.buildTreeUtil(inorder,postorder,start_index,end_index,preIndex)
        return  res 