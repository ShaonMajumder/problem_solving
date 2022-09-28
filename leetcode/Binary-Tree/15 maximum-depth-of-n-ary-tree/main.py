# https://leetcode.com/problems/maximum-depth-of-n-ary-tree
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        def depth(root,n):
            if root:
                if root.children:
                    arr = []
                    n = n + 1
                    for x in root.children:
                        arr = arr + depth(x,n)

                    if n == 1:
                        return max(arr)
                    else:
                        return arr
                else:
                    n = n + 1
                    if n == 1:
                        return n
                    else:
                        return [n]
            else:
                if n == 0:
                    return 0
            
        return depth(root,0)

root = Node(1, [Node(3, [Node(5), Node(6)] ), Node(2), Node(4)] )
p = Solution()
print( p.maxDepth(root) )