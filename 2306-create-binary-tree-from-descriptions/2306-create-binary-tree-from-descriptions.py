# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        valid = {}
        parent = {}
        for i in descriptions:
            parent[i[1]]=0
            parent[i[0]]=0

        for i in descriptions:
            if i[0] not in valid:
                valid[i[0]]=TreeNode(i[0])
            if i[1] not in valid:
                valid[i[1]]=TreeNode(i[1])
            if i[2]==1:
                valid[i[0]].left=valid[i[1]]
            else:
                valid[i[0]].right = valid[i[1]]
            parent[i[1]]=1
        for i in parent:
            if parent[i]==0:
                return valid[i]
                    


                

        