# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def sum1(node,sum):
            if sum==targetSum and node is None:
                print(sum)
                return True 
            else:
                print(sum)
                if node.left and node.right:
                    return (sum1(node.left,sum+node.val) or sum1(node.right,sum+node.val))
                elif node.left:
                    return sum1(node.left,sum+node.val)
                elif node.right:
                    return sum1(node.right,sum+node.val)
                else:
                    if node.val+sum==targetSum:
                        return True
                    return False
                
            
        return (sum1(root,0)==True)
            

            
