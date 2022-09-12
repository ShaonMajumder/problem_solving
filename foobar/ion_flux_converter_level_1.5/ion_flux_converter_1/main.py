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
# https://stackoverflow.com/questions/28846377/what-is-the-difference-btw-order-and-degree-in-terms-of-tree-data-structure
# https://www.google.com/search?q=nodes+of+binary+tree&oq=nodes+of+bi&aqs=chrome.0.0i20i263i512j0i512l2j69i57j0i15i22i30l2j0i22i30l4.6594j1j7&sourceid=chrome&ie=UTF-8
# https://www.andrew.cmu.edu/course/15-121/lectures/Trees/trees.html#:~:text=A%20binary%20tree%20is%20made,node%20is%20called%20a%20parent.
# https://www.geeksforgeeks.org/level-order-tree-traversal/
# https://towardsdatascience.com/google-foobar-challenge-level-1-3487bb252780
# https://www.quora.com/What-is-the-use-of-pre-order-and-post-order-traversal-of-binary-trees-in-computing
