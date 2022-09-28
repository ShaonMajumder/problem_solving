# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], n = 0) -> int:
        if root:
            n = n + 1
            lefth = self.maxDepth( root.left,n)
            righth = self.maxDepth( root.right,n)
            if lefth > righth:
                return lefth
            else:
                return righth   
        else:
            return n