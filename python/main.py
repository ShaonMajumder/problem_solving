# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
         
 
# Driver code
root = Node(14)
root.left = Node(16)
root.left.left = Node(66)
root.left.left.left = Node(33)
root.left.left.right = Node(45)

root.right = Node(41)
root.right.right = Node(50)
root.right.right.right = Node(35)
root.right.left = Node(76)



 
print ("\nInorder traversal of binary tree is")
printInorder(root)