class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        from collections import defaultdict
        
        # Build the tree using an adjacency list
        tree = defaultdict(list)
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        
        # Function to calculate the subtree sum and number of nodes
        def dfs(node: int):
            total_sum = value[node]
            total_nodes = 1
            for child in tree[node]:
                child_sum, child_count = dfs(child)
                total_sum += child_sum
                total_nodes += child_count
            # If subtree sum is zero, we count it as removed
            if total_sum == 0:
                return 0, 0
            return total_sum, total_nodes
        
        total_sum, total_nodes = dfs(0)
        
        return total_nodes