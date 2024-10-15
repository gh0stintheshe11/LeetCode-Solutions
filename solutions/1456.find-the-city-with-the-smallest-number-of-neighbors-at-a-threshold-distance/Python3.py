class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the Floyd-Warshall distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Set the distance from each city to itself as 0
        for i in range(n):
            dist[i][i] = 0
            
        # Set the distances based on the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Apply Floyd-Warshall algorithm to find the shortest paths between every pair of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Determine number of reachable neighbors within distance threshold for each city
        minReachableCities = float('inf')
        cityWithMinReachable = -1
        
        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            # If there's a tie, pick the city with the greater index
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                cityWithMinReachable = i
        
        return cityWithMinReachable