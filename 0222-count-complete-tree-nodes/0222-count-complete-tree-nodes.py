# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack=[root]
        length=0
        while stack:
            temp=stack.pop()
            if temp:
                length+=1
                stack.append(temp.left)
                stack.append(temp.right)
        return length

        