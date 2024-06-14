# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(Node):
            if Node is None:
                return 0
            else:
                return 1+max(height(Node.left),height(Node.right))
        if root is None :
            return True
        if root.left is None and root.right is None:
            return True
        if(abs(height(root.left)-height(root.right)) <=1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
