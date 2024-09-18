# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum=0
        if root is None:
            return sum
        def sumleaves(root,flag):

            if root.left and root.right:
                return sum+sumleaves(root.left,0)+sumleaves(root.right,1)
            elif root.left:
                return sum+sumleaves(root.left,0)
            elif root.right:
                return sum+sumleaves(root.right,1)
            else:
                if flag==0:
                    return sum+root.val
                else:
                    return sum
                
        return sumleaves(root,1)
                
        