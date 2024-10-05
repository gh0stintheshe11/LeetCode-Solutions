from collections import Counter
from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def backtrack(half: str, visited: List[bool], path: str, res: List[str]):
            if len(path) == len(half):
                res.append(path)
                return
            for i in range(len(half)):
                if visited[i] or (i > 0 and half[i] == half[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                backtrack(half, visited, path + half[i], res)
                visited[i] = False

        count = Counter(s)
        mid = [char for char, cnt in count.items() if cnt % 2]
        if len(mid) > 1:
            return []
        
        mid = '' if not mid else mid[0]
        half = ''.join([char * (cnt // 2) for char, cnt in count.items()])
        res = []
        visited = [False] * len(half)
        half_permutations = []
        backtrack(half, visited, '', half_permutations)
        return [hp + mid + hp[::-1] for hp in half_permutations]