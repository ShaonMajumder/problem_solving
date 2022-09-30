# https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        childrens=[]
        
        if root.children:
             
            childrens = [root.val]
            childrens.append( [self.postorder(x) for x in root.children] )
            print(childrens)
            return childrens
        else:
            return root.val
        


root = Node(1, [Node(3, [Node(5), Node(6)] ), Node(2), Node(4)] )
p = Solution()
print( p.postorder(root) )

