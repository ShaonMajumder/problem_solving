# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        def preorder(root):
            if root:
                return [root.val] + preorder(root.left) + preorder(root.right)
            else:
                return []
        return preorder(root)

#organized in preorder, as we draw tree
# [1,null,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

p = Solution()
print( p.preorderTraversal(root) )