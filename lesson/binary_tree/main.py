
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
# A function to do preorder tree traversal
def getPreorder(root):
    if root:
        return [root.val] + getPreorder(root.left) + getPreorder(root.right)
    else:
        return []

# A function to do inorder tree traversal
def getInorder(root):
    if root:
        return getInorder(root.left) + [root.val] + getInorder(root.right)
    else:
        return []
  
  
# A function to do postorder tree traversal
def getPostorder(root):
    if root:
        return getPostorder(root.left) + getPostorder(root.right) + [root.val]
    else:
        return []
  
  
def getHeight(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
#   1
#  2 3
# 4 5
# reach to nodes
# 1 2 4 5 3 preorder
# 4 2 5 1 3 inorder
# 4 5 2 3 1 post order

# Driver code
root = Node(7)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)

print("Preorder traversal of binary tree is")
print(getPreorder(root))

print("\nInorder traversal of binary tree is")
print(getInorder(root))
  
print ("\nPostorder traversal of binary tree is")
print(getPostorder(root))

print( "Height")
print(getHeight(root))