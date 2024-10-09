class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            current_time += time
            total_waiting_time += current_time - arrival
        
        return total_waiting_time / len(customers)