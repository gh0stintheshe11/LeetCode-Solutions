class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                return True
            return False

        parent = {}
        count = 0
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r, c in positions:
            if (r, c) in parent:
                result.append(count)
                continue
            
            parent[(r, c)] = (r, c)
            count += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:
                    if union((r, c), (nr, nc)):
                        count -= 1

            result.append(count)

        return result