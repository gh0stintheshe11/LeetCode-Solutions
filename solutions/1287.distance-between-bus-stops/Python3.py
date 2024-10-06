class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        clockwise_distance = sum(distance[start:destination])
        total_distance = sum(distance)
        
        return min(clockwise_distance, total_distance - clockwise_distance)