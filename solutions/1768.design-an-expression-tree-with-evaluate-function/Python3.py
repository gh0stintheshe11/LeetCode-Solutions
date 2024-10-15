import abc
from abc import ABC, abstractmethod
from typing import List

# Node class interface which is an abstract base class
class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass

# NumericNode class to represent operands in the tree
class NumericNode(Node):
    def __init__(self, value: int):
        self.value = value
    
    def evaluate(self) -> int:
        return self.value

# OperatorNode class to represent operators in the tree
class OperatorNode(Node):
    def __init__(self, left: Node, right: Node, operator: str):
        self.left = left
        self.right = right
        self.operator = operator

    def evaluate(self) -> int:
        if self.operator == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.operator == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.operator == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.operator == '/':
            return self.left.evaluate() // self.right.evaluate()

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        
        for token in postfix:
            if token.isdigit():
                node = NumericNode(int(token))
                stack.append(node)
            else:
                right = stack.pop()
                left = stack.pop()
                node = OperatorNode(left, right, token)
                stack.append(node)
        
        return stack.pop()

# Example usage:
# obj = TreeBuilder()
# expTree = obj.buildTree(["3", "4", "+", "2", "*", "7", "/"])
# ans = expTree.evaluate()  # Output: 2