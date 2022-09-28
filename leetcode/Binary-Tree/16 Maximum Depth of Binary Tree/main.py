# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root,n):
            if root:
                n = n + 1
                lefth = depth(root.left,n)
                righth = depth(root.right,n)
                if lefth > righth:
                    return lefth
                else:
                    return righth   
            else:
                return n
        return depth(root,0)