from typing import List
from collections import defaultdict
import itertools

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # Union-Find class to handle synonym groups
        class UnionFind:
            def __init__(self):
                self.parent = {}
                
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    self.parent[rootY] = rootX
        
        uf = UnionFind()
        
        # Initialize Union-Find
        for a, b in synonyms:
            if a not in uf.parent:
                uf.parent[a] = a
            if b not in uf.parent:
                uf.parent[b] = b
            uf.union(a, b)
        
        # Create a root to group mapping
        groups = defaultdict(list)
        for word in uf.parent:
            root = uf.find(word)
            groups[root].append(word)
        
        # Sort each group for lexicographical order
        for root in groups:
            groups[root].sort()
        
        # Split text into words
        words = text.split()
        
        # Backtracking to generate all possible sentences
        def backtrack(index, path):
            if index == len(words):
                results.append(' '.join(path))
                return
            current_word = words[index]
            if current_word in uf.parent:
                root = uf.find(current_word)
                for synonym in groups[root]:
                    backtrack(index + 1, path + [synonym])
            else:
                backtrack(index + 1, path + [current_word])
        
        results = []
        backtrack(0, [])
        results.sort()
        return results