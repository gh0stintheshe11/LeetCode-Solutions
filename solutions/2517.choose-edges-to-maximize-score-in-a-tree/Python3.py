class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        edge_map = {i: [] for i in range(len(edges))}
        for i, edge in zip(range(1, len(edges)), edges[1:]):
            edge_map[edge[0]].append((i, edge[1]))

        lookup = {}
        def dfs(node, can_be_considered):
            if (node, can_be_considered) in lookup:
                return lookup[(node, can_be_considered)]

            max_score = 0
            if can_be_considered:
                # choice of whether to consider an edge of one of the neighbors or 
                # not to consider any edge at all of the neighbors

                # when a single edge is considered
                for i in range(len(edge_map[node])):
                    nei, score = edge_map[node].pop(i)
                    if score > 0:
                        x = score + dfs(nei, False)
                    else:
                        x = dfs(nei, True)

                    y = 0
                    for item in edge_map[node]:
                        n, s = item[:]
                        y += dfs(n, True)
                    max_score = max(max_score, x + y)
                    edge_map[node].insert(i, (nei, score))

                # when no edge is considered
                z = 0
                for tup in edge_map[node]:
                    nei, score = tup
                    z += dfs(nei, True)
                max_score = max(max_score, z)
                
            else:
                z = 0
                for tup in edge_map[node]:
                    nei, score = tup
                    z += dfs(nei, True)
                max_score = max(max_score, z)
            lookup[(node, can_be_considered)] = max_score
            return max_score
            
        return dfs(0, True)