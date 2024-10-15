"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_uniform(grid, x, y, length):
            val = grid[x][y]
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != val:
                        return False, val
            return True, val

        def construct_rec(x, y, length):
            if length == 1:
                return Node(grid[x][y] == 1, True, None, None, None, None)
            
            half_length = length // 2
            
            topLeftNode = construct_rec(x, y, half_length)
            topRightNode = construct_rec(x, y + half_length, half_length)
            bottomLeftNode = construct_rec(x + half_length, y, half_length)
            bottomRightNode = construct_rec(x + half_length, y + half_length, half_length)

            if (topLeftNode.isLeaf and topRightNode.isLeaf and 
                bottomLeftNode.isLeaf and bottomRightNode.isLeaf and
                topLeftNode.val == topRightNode.val == bottomLeftNode.val == bottomRightNode.val):
                return Node(topLeftNode.val, True, None, None, None, None)
            else:
                return Node(True, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)
        
        n = len(grid)
        return construct_rec(0, 0, n)