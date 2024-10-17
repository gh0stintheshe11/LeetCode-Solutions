class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        neighbours = defaultdict(set)
        cycles = 0

        for room1, room2 in corridors:
            neighbours[room1].add(room2)
            neighbours[room2].add(room1)
            cycles += len(neighbours[room1].intersection(neighbours[room2]))

        return cycles