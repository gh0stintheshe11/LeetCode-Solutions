class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        seen = set()
        result = []
        
        for query in reversed(queries):
            if query not in seen:
                seen.add(query)
                result.append(query)
        
        for window in windows:
            if window not in seen:
                result.append(window)
        
        return result