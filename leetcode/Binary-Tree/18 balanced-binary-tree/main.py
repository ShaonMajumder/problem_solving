# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], n = 0) -> bool:
        if root:
            n = n + 1
            lefth = self.isBalanced( root.left,n)
            righth = self.isBalanced( root.right,n)
            
            if lefth == False or righth == False:
                return False
            elif abs(lefth - righth) > 1:
                return False
            elif lefth > righth:
                return lefth
            else:
                return righth   
        else:
            if n == 0:
                return True
            return n