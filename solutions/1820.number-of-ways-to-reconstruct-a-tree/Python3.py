class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Build the adjacency list
        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)
        
        # Find the potential root
        all_nodes = set(adj.keys())
        root = -1
        for node in adj:
            if len(adj[node]) == len(all_nodes) - 1:
                root = node
                break

        if root == -1:
            return 0
        
        result = 1

        # Check every node and attempt to find its parent
        for node in adj:
            if node == root:
                continue
            
            # Find the candidate parent
            potential_parents = []
            for neighbor in adj[node]:
                if len(adj[neighbor]) >= len(adj[node]):
                    potential_parents.append(neighbor)
            
            if not potential_parents:
                return 0
            
            # Select parent as the one with the minimum degree (smallest connected component)
            parent = min(potential_parents, key=lambda x: len(adj[x]))

            # Check if node is connected to the potential parent
            if node in adj[parent]:
                # Check if all connections of this node are a subset of parent
                if all(neighbor in adj[parent] for neighbor in adj[node] if neighbor != parent):
                    if len(adj[parent]) == len(adj[node]):
                        result = 2  # More than one way
                else:
                    return 0
            else:
                return 0

        return result