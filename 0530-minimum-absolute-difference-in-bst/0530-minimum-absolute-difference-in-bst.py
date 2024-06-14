# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        a=[]
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
            def inorder(self,Node):
                if Node is None:
                    return None


                if Node.left is not None:
                    self.inorder(Node.left)
                a.append(Node.val)
                if Node.right is not None:
                    self.inorder(Node.right)

        b=TreeNode()
        b.inorder(root)
        k=a[1]-a[0]
        for i in range(1,len(a)):
            if abs(a[i]-a[i-1])<k:
                k=abs(a[i]-a[i-1])
        return k


        

