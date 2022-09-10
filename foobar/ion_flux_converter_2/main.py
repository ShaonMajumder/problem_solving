from multiprocessing import parent_process
from platform import node


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def printInorder(root):
    arr = []
    if root:
        arr = arr + printInorder(root.left)
        arr = arr + [root.val]
        arr = arr + printInorder(root.right)
        return arr
    else:
        return []
  
def printPostorder(root):
    arr = []
    if root:
        arr = arr + printPostorder(root.left)
        arr = arr + printPostorder(root.right)
        arr = arr + [root.val]
        return arr
    else:
        return []
  
def printPreorder(root):
    arr = []
    if root:
        arr = arr + [root.val]
        arr = arr + printPreorder(root.left)
        arr = arr + printPreorder(root.right)
        return arr
    else:
        return []
  
# Python3 Program to print binary tree in 2D
COUNT = [10]
 
# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


def isBalanced(root):
 
    # Base condition
    if root is None:
        return True
 
    # Compute height of left subtree
    lh = isBalanced(root.left)
 
    # If left subtree is not balanced,
    # return -1
    if lh == -1:
        return -1
 
    # Do same thing for the right subtree
    rh = isBalanced(root.right)
    if rh == -1:
        return -1
 
    # Allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) > 1):
        return -1
 
    # If we reach here means tree is
    # height-balanced tree, return height
    # in this case
    else:
        return max(lh, rh) + 1
        
def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)

# printPreorder(tree)
# Driver code
root = Node(7)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)

def getPerfectBinaryTree(height):
    def tree(key,height):
        # print(f"call tree({key},{height})")
        
        if height > 1:
            height-=1
            root = Node(key)
            root.left = tree(key - 2**height, height) 
            root.right = tree(key - 1, height)
            return root
        else:
            # print(f"leaf Node {key}")
            return Node(key)
            
    # 2**height - 1
    return tree(2**height - 1,height)
    

trees = getPerfectBinaryTree(5)
print_tree(trees)
# print(trees)
order = printPreorder(trees)

print(order.index(19)+1)

# print("Preorder traversal of binary tree is")
# printPreorder(root)
# print("\nInorder traversal of binary tree is")
# printInorder(root)
# print("\nPostorder traversal of binary tree is")
# printPostorder(root)