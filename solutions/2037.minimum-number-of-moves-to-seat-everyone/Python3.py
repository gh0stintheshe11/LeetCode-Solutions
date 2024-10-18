from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both the seats and students arrays
        seats.sort()
        students.sort()
        
        # Initialize the total number of moves to 0
        total_moves = 0
        
        # Calculate the total number of moves required
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        
        return total_moves