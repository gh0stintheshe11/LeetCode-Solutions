class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        # Helper function to find the root of a word
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Helper function to union two words
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        parent = {}
        
        # Initialize the Disjoint Set Union (DSU)
        for x, y in similarPairs:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            union(x, y)
        
        # Check each pair in the sentences
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if w1 not in parent or w2 not in parent or find(w1) != find(w2):
                return False
        
        return True