class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        from collections import defaultdict

        # Build the tree adjacency list
        tree = defaultdict(list)
        for child in range(1, len(parent)):
            tree[parent[child]].append(child)

        self.max_path = 1

        def dfs(node):
            max1, max2 = 0, 0  # Initialize two maximum lengths

            # Explore all children
            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:  # Only consider paths with different characters
                    if child_length > max1:
                        max2 = max1
                        max1 = child_length
                    elif child_length > max2:
                        max2 = child_length

            # Update the max path considering the two longest different-character child-paths
            self.max_path = max(self.max_path, max1 + max2 + 1)

            return max1 + 1

        dfs(0)
        return self.max_path