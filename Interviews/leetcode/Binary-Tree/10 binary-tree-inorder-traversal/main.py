# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []
        return inorder(root)

#organized in preorder, as we draw tree
# [1,null,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

p = Solution()
print( p.inorderTraversal(root) )