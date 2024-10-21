from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        self.edge_map = defaultdict(set)
        for edge in edges:
            self.edge_map[edge[0]].add(edge[1])
            self.edge_map[edge[1]].add(edge[0])

        def removeEdge(src, next_src):
            self.edge_map[src].remove(next_src)
            self.edge_map[next_src].remove(src)

        @lru_cache(maxsize=None)
        def getShortestPath(src, dest) -> list:
            if src == dest:
                return (src,)
            seen = set([src])
            dad_map = {}
            dad_map[src] = None
            cur_nodes = [src]
            while cur_nodes:
                next_nodes = []
                for node in cur_nodes:
                    neigh_nodes = self.edge_map[node]
                    for neigh in neigh_nodes:
                        if neigh not in seen:
                            next_nodes.append(neigh)
                            dad_map[neigh] = node
                            seen.add(neigh)      
                            if neigh == dest:
                                res = []
                                while dest is not None:
                                    res.append(dest)
                                    dest = dad_map[dest]
                                return res[::-1]      
                cur_nodes = next_nodes 

        vals = [i for i in self.edge_map if len(self.edge_map[i]) == 1]
        if len(vals) > 0:
            src = vals[0]
            dest = vals[1]
        else:
            vals = [i for i in self.edge_map if len(self.edge_map[i]) == 2]
            src = vals[0]
            path_len = []
            for dest in vals:
                cur_path = getShortestPath(src, dest)
                path_len.append((len(cur_path), dest))
            path_len.sort()
            dest = path_len[2][1]

        first_row = getShortestPath(src, dest)
        row_count = n // len(first_row)

        for i in range(len(first_row) - 1):
            removeEdge(first_row[i], first_row[i + 1])

        final_res = [first_row]
        for _ in range(1, row_count):
            cur_row = []
            for j in range(len(first_row)):
                prev_val = final_res[-1][j]
                cur_val = self.edge_map[prev_val]
                cur_val = list(cur_val)[0]
                cur_row.append(cur_val)
                removeEdge(prev_val, cur_val)
            for i in range(len(first_row) - 1):
                removeEdge(cur_row[i], cur_row[i + 1])
            final_res.append(tuple(cur_row))

        return final_res