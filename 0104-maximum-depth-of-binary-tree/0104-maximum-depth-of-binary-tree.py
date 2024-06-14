# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(Node):
            if Node is None:
                return 0
            else:
                return 1+max(height(Node.right),height(Node.left))
        return height(root)