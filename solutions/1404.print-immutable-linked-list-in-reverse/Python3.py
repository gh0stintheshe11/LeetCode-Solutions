class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # Helper function to perform DFS
        def dfs(node):
            if node is None:
                return
            dfs(node.getNext())
            node.printValue()
        
        # Start DFS from the head
        dfs(head)