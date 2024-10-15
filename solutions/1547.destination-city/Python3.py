class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_cities = set(cityA for cityA, cityB in paths)
        for cityA, cityB in paths:
            if cityB not in outgoing_cities:
                return cityB