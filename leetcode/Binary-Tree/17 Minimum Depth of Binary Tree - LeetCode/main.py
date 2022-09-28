# https://leetcode.com/problems/minimum-depth-of-binary-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root, n=0) -> int:
        if root:
            n = n + 1
            lefth = self.minDepth( root.left,n)
            righth = self.minDepth( root.right,n)
            if lefth and righth:
                if lefth < righth:
                    return lefth
                else:
                    return righth
            elif lefth:
                return lefth
            elif righth:
                return righth
            else:
                return n
        else:
            return 0

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

[2,None,3,None,4,None,5,None,6]


root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

p = Solution()
print(p.minDepth(root))