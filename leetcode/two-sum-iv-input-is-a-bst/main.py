# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k):
        arr = []
        def read_(root):
            if root:
                read_(root.left)
                read_(root.right)
                arr.append(root.val)
            

        read_(root)
        for i in range(0,len(arr)) :
            for j in range(i+1,len(arr)):
                if arr[i] + arr[j] == k:
                    return True
        return False



root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)


s = Solution()
print( s.findTarget(root,9) )