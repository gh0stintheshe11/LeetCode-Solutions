from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Create a reverse adjacency list
        reverse_adj_list = defaultdict(list)
        for u, v in edges:
            reverse_adj_list[v].append(u)

        # Function to perform BFS and find all ancestors
        def find_ancestors(node):
            ancestors = set()
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for predecessor in reverse_adj_list[current]:
                    if predecessor not in ancestors:
                        ancestors.add(predecessor)
                        queue.append(predecessor)
            return sorted(ancestors)

        # Generate the list of ancestors for each node
        result = []
        for i in range(n):
            result.append(find_ancestors(i))
        return result