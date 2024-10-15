class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)
        
        for first, last, seats in bookings:
            answer[first - 1] += seats
            answer[last] -= seats
        
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
        return answer[:-1]