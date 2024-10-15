from typing import List, Set, Tuple, Dict

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        from collections import defaultdict, deque

        n = len(edges) + 1

        # Graph representation of tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Convert guesses to a set for O(1) query
        guess_set = set((u, v) for u, v in guesses)

        # Initial DFS to compute correct guesses with 0 as root
        def dfs(node: int, parent: int) -> int:
            count = 0
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                count += dfs(neighbor, node) + ((node, neighbor) in guess_set)
            return count

        initial_correct = dfs(0, -1)

        # Rerooting DFS
        result = 0

        def reroot(node: int, parent: int, correct: int) -> None:
            nonlocal result
            # If correct is >= k, then node can be a root
            if correct >= k:
                result += 1
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                # Calculate new correct count for the child as the new root
                new_correct = correct
                if (node, neighbor) in guess_set:
                    new_correct -= 1
                if (neighbor, node) in guess_set:
                    new_correct += 1
                reroot(neighbor, node, new_correct)

        reroot(0, -1, initial_correct)

        return result