# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        def getValIndex(s, start):
            end = start
            if s[end] == '-':
                end += 1
            while end < len(s) and s[end].isdigit():
                end += 1
            return int(s[start:end]), end
        
        def buildTree(s, start, end):
            if start > end:
                return None
            
            val, index = getValIndex(s, start)
            node = TreeNode(val)
            
            if index <= end and s[index] == '(':
                balance = 1
                left_end = index + 1
                while balance != 0:
                    if s[left_end] == '(':
                        balance += 1
                    elif s[left_end] == ')':
                        balance -= 1
                    left_end += 1
                node.left = buildTree(s, index + 1, left_end - 2)
                if left_end <= end and s[left_end] == '(':
                    node.right = buildTree(s, left_end + 1, end - 1)
            return node
        
        return buildTree(s, 0, len(s) - 1)