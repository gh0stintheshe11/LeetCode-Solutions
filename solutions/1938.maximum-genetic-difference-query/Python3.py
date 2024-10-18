from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        def insert(x: int):
            node = root
            for i in range(20, -1, -1):
                bit = (x >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1

        def remove(x: int):
            node = root
            for i in range(20, -1, -1):
                bit = (x >> i) & 1
                node = node.children[bit]
                node.count -= 1

        def max_xor(x: int) -> int:
            node = root
            ans = 0
            for i in range(20, -1, -1):
                bit = (x >> i) & 1
                opposite_bit = 1 - bit
                if opposite_bit in node.children and node.children[opposite_bit].count > 0:
                    ans |= (1 << i)
                    node = node.children[opposite_bit]
                else:
                    node = node.children[bit]
            return ans

        n = len(parents)
        tree = defaultdict(list)
        rootIdx = None

        for child, parent in enumerate(parents):
            if parent == -1:
                rootIdx = child
            else:
                tree[parent].append(child)

        max_queries = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            max_queries[node].append((val, i))

        results = [0] * len(queries)
        root = TrieNode()

        def dfs(node: int):
            insert(node)

            if node in max_queries:
                for val, idx in max_queries[node]:
                    results[idx] = max_xor(val)

            for child in tree[node]:
                dfs(child)

            remove(node)

        dfs(rootIdx)
        return results