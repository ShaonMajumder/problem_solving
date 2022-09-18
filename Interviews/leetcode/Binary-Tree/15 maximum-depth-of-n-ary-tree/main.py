
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        def depth(root,n=0):
            if root:
                if root.children:
                    n = n + 1
                    for x in root.children:
                        n = depth(x,n)
                return n
            else:
                return 0
                
                    
        
        return depth(root,0) + 1
        

root = Node(1, [Node(3, [Node(5), Node(6)] ), Node(2), Node(4)] )
root2 = Node(1, [ Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])] ), Node(4), Node(5) ] )
p = Solution()
print( p.maxDepth(root) )

