class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m+1))
        result = []
        for query in queries:
            pos = P.index(query)
            result.append(pos)
            P.insert(0, P.pop(pos))
        return result