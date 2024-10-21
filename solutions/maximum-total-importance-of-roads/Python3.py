class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Calculate the degree of each city
        degree = defaultdict(int)
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Sort cities by their degree in decreasing order
        sorted_cities = sorted(degree.keys(), key=lambda x: degree[x], reverse=True)
        
        # Assign values from n to 1 based on sorted order by degree
        importance = {}
        value = n
        for city in sorted_cities:
            importance[city] = value
            value -= 1
        
        # If there are any cities not in the roads at all, assign them the next available values (lower ones)
        for city in range(n):
            if city not in importance:
                importance[city] = value
                value -= 1

        # Calculate the total maximum importance
        total_importance = 0
        for a, b in roads:
            total_importance += importance[a] + importance[b]
        
        return total_importance