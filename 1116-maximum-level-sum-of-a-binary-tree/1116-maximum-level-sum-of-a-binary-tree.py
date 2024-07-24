# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def levelorder(root,level):
            if root is None:
                return 
            if len(ans)<level:
                ans.append(0)
            ans[level-1]+=root.val
            levelorder(root.left,level+1)
            levelorder(root.right,level+1)
        levelorder(root,1)
        return ans.index(max(ans))+1


        