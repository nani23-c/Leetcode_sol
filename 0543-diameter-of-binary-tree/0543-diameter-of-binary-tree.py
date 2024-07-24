# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def Diameter(node,maxi):
            if not node:
                return 0 
            left = Diameter(node.left,maxi)
            right = Diameter(node.right,maxi)
            maxi[0] = max(maxi[0],left+right)
            return max(left,right)+1
        Diameter(root,maxi)
        return maxi[0]
            

        