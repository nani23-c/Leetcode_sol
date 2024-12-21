# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def Traverse(leftnode,rightnode,Level):
            if leftnode:
                if Level%2==1:
                    leftnode.val,rightnode.val=rightnode.val,leftnode.val
                Traverse(leftnode.left,rightnode.right,Level+1)
                Traverse(leftnode.right,rightnode.left,Level+1)
        Traverse(root.left,root.right,1)
        return root

            
