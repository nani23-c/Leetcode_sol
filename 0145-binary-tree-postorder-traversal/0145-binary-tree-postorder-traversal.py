# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        def preorder(Node):
            if Node:
                
                if Node.left:
                    preorder(Node.left)
                if Node.right:
                    preorder(Node.right)
                pre.append(Node.val)
        preorder(root)
        return pre
        