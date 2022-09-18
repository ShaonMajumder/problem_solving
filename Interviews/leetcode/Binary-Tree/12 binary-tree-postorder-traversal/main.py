# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        def postorder(root):
            if root:
                return postorder(root.left) + postorder(root.right) + [root.val]
            else:
                return []
        return postorder(root)

#organized in postorder, as we draw tree
# [1,null,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

p = Solution()
print( p.postorderTraversal(root) )