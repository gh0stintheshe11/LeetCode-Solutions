class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev_occupied = -1
        max_distance = 0
        
        for i in range(n):
            if seats[i] == 1:
                if prev_occupied == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, (i - prev_occupied) // 2)
                prev_occupied = i
        
        max_distance = max(max_distance, n - 1 - prev_occupied)
        
        return max_distance