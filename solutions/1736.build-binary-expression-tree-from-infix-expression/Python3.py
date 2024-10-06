# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def constructTreeFromPostfix(postfix):
            stack = []
            for char in postfix:
                if char.isdigit():
                    stack.append(Node(char))
                else:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(Node(char, left, right))
            return stack[-1]

        def infixToPostfix(expression):
            stack = []
            output = []
            for char in expression:
                if char.isdigit():
                    output.append(char)
                elif char == '(':
                    stack.append(char)
                elif char == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()
                else:
                    while stack and precedence(stack[-1]) >= precedence(char):
                        output.append(stack.pop())
                    stack.append(char)
            while stack:
                output.append(stack.pop())
            return output
        
        postfix = infixToPostfix(s)
        return constructTreeFromPostfix(postfix)