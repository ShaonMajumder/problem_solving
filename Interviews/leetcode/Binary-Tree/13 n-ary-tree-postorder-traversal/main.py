
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        childrens=[]
        if root:
            if root.children:
                for x in root.children:
                    childrens = childrens + self.postorder(x)
                return childrens + [root.val]
            else:
                return [root.val]
        else:
            return []
        


root = Node(1, [Node(3, [Node(5), Node(6)] ), Node(2), Node(4)] )
p = Solution()
print( p.postorder(root) )

