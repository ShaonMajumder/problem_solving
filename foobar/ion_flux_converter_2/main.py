from multiprocessing import parent_process
from platform import node

import math

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def getInorder(root):
    arr = []
    if root:
        arr = arr + getInorder(root.left)
        arr = arr + [root.val]
        arr = arr + getInorder(root.right)
        return arr
    else:
        return []
  
def getPostorder(root):
    arr = []
    if root:
        arr = arr + getPostorder(root.left)
        arr = arr + getPostorder(root.right)
        arr = arr + [root.val]
        return arr
    else:
        return []
  
def getPreorder(root):
    arr = []
    if root:
        arr = arr + [root.val]
        arr = arr + getPreorder(root.left)
        arr = arr + getPreorder(root.right)
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

def draw_tree(root, val="val", left="left", right="right"):
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

# print(order.index(14))

# print("Preorder traversal of binary tree is")
# getPreorder(root)
# print("\nInorder traversal of binary tree is")
# getInorder(root)
# print("\nPostorder traversal of binary tree is")
# getPostorder(root)

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
    return tree( totalNodeCountPerfectBinaryTree(height) ,height)
    
def leafNodeCountPerfectBinaryTree(height):
    return 2**(height - 1)

def totalNodeCountPerfectBinaryTree(height):
    return 2**height - 1

trees = getPerfectBinaryTree(5)
draw_tree(trees)
order = getInorder(trees)





# is left
# 2**height - 1 = ParentNode
# ParentNode + 1 = 2**height
def element_is_left(key):
    # key + 1 = 2**height
    log_ = math.log(key+1,2)
    # is a whole number ?
    if log_.is_integer():
        return True
    elif( (key >> 1) % 2 == 0):
        # Just before becoming a perfect power of 2, if node was equal to 2 * x, then it was right child.
        return False
    else:
        return True



# 2**height - 1 = ParentNode
# ParentNode + 1 = 2**height
# logof2(node + 1) = height
# Thus if node + 1 is perfect power of 2 then we can find out the height easily. 
# (No need to take log base 2, just see the number of bits after converting to binary).
def getHeightOfConverter(node):
    # print(f"getHeightOfConverter({node})")
    k = math.log(node + 1, 2) 
    # print(f"k={k}")
    if k.is_integer():
        return k
    else:
        i = math.floor( math.log(node,2))
        x = 2**i - 1
        return getHeightOfConverter(node - x)
    
    




def solution(h,q):
    
    def func(node):

        node_height = getHeightOfConverter(node)
        if node_height == h:
            return -1
        
        if element_is_left(node):
            node_label = 2**node_height + node
        else:
            node_label = node + 1

        return int(node_label)
    return [ func(i) for i in q]

print(solution(3,[1,4,7]))
print(solution(5,[19, 14, 28]))
print( element_is_left(14) )

# Just before becoming a perfect power of 2, if node was equal to 2 * x, then it was right child.






