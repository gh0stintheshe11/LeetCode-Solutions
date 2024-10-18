class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        def dfs(node: int, parent: int) -> int:
            subtree_size = 1
            child_sizes = []
            for child in tree[node]:
                if child != parent:
                    child_size = dfs(child, node)
                    child_sizes.append(child_size)
                    subtree_size += child_size
            if len(set(child_sizes)) <= 1:
                self.good_count += 1
            return subtree_size
        
        n = len(edges) + 1
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        self.good_count = 0
        dfs(0, -1)
        return self.good_count