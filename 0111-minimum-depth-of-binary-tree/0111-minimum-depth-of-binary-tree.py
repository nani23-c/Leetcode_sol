# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        def depth(Node):
            if Node is None:
                return 0
            
            if Node.left and Node.right:
                return  1+min(depth(Node.left),depth(Node.right))
            else:
                return 1+max(depth(Node.left),depth(Node.right))
        return depth(root)