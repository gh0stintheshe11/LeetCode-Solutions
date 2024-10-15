class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        total_distance = 0
        max_diff = float('-inf')
        
        for nut in nuts:
            distance_to_tree = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            distance_to_squirrel = abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])
            total_distance += 2 * distance_to_tree
            max_diff = max(max_diff, distance_to_tree - distance_to_squirrel)
        
        return total_distance - max_diff