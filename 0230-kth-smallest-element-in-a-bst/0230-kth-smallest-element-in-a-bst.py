# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        Nodes = []
        def Traversal(node):
            if node is None:
                return 
            Traversal(node.left)
            Nodes.append(node.val)
            Traversal(node.right)
        Traversal(root)
        return Nodes[k-1]

        