
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        childrens=[]
        if root:
            if root.children:
                for x in root.children:
                    childrens = childrens + self.preorder(x)
            return [root.val] + childrens
        else:
            return []

root = Node(1, [Node(3, [Node(5), Node(6)] ), Node(2), Node(4)] )
p = Solution()
print( p.preorder(root) )

