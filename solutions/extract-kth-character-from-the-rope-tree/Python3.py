class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        return self.getSNode(root)[k-1]

    def getSNode(self, node: Optional[object]) -> str:
        if node is None:
            return ""
        elif self.isLeaf(node):
            return node.val
        elif self.isInternal(node):
            return (self.getSNode(node.left) + self.getSNode(node.right))
        else:
            return ""

    def isLeaf(self, node: Optional[object]) -> bool:
        return node.left is None and node.right is None
    
    def isInternal(self, node: Optional[object]) -> bool:
        return node.left is not None or node.right is not None