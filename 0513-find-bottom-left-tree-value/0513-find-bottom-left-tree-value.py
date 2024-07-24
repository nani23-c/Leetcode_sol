# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [[]]
        def levelorder(root,max):
            if root is None:
                return 
            if len(ans)<max:
                ans.append([])
            ans[max-1].append(root.val)
            levelorder(root.left,max+1)
            levelorder(root.right,max+1)
        levelorder(root,1)
        return ans[-1][0]

            
        