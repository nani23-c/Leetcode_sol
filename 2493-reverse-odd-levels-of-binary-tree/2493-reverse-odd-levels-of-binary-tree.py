# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        ans_level = [0]
        def LevelOrder(Node,Level):
            if Level==ans_level[0]:
                ans_level[0]+=1
                ans.append([])
            ans[Level].append(Node.val)
            if Node.left:  
                Level+=1
                LevelOrder(Node.left,Level)
                LevelOrder(Node.right,Level)
        LevelOrder(root,0)
        for i in range(len(ans)):
            if i%2!=0:
                ans[i].reverse()
        print(ans)
        def Equal(Node,Level):
            Node.val=ans[Level].pop(0)
            if Node.left:
                Level+=1
                Equal(Node.left,Level)
                Equal(Node.right,Level)
        Equal(root,0)
        return root


            
