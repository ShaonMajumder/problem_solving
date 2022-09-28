# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getInorder(self,root):
        if root:
            return self.getInorder(root.left) + [root.val] + self.getInorder(root.right)
        else:
            return []
            
    def inorderTraversal(self, root):
        trees = p.insertLevelOrder(root, 0, len(root))
        return self.getInorder(trees)

    # Function to insert nodes in level order 
    def insertLevelOrder(self,arr, i, n):
        root = None
        # Base case for recursion 
        if i < n:
            root = TreeNode(arr[i]) 
    
            # insert left child 
            root.left = self.insertLevelOrder(arr, 2 * i + 1, n)
    
            # insert right child 
            root.right = self.insertLevelOrder(arr, 2 * i + 2, n)
            
        return root
  

  

arr = [1,None,2,3]
n = len(arr)

p = Solution()
ans = p.inorderTraversal(arr)
print(ans)