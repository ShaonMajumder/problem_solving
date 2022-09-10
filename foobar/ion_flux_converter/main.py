# h of the tree
#  n(p) == n(q)
# if no label -1

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def getPostorder(root):
    if root:
        getPostorder(root.left)
        getPostorder(root.right)
        print(root.val)
  
  
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def getLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        getCurrentLevel(root, i)
 
def getCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        getCurrentLevel(root.left, level-1)
        getCurrentLevel(root.right, level-1)

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


  
print("Postorder traversal of binary tree is")
getPostorder(root)
print("Height of the tree")
print( height(root) )

print("Level order traversal of binary tree is -")
getLevelOrder(root)

print("\nrexo")

h = 3
while h > 0:
    print(2**h - 1)
    h-=1
