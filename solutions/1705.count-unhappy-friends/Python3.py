class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j, friend in enumerate(preferences[i]):
                rank[i][friend] = j

        pair_map = {}
        for x, y in pairs:
            pair_map[x] = y
            pair_map[y] = x
        
        unhappy_count = 0
        
        for x in range(n):
            y = pair_map[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = pair_map[u]
                if rank[u][x] < rank[u][v]:
                    unhappy_count += 1
                    break
        
        return unhappy_count