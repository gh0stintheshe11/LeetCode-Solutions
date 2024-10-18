class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        arrive, i = 0, 0
        passenger_set = set(passengers)  

        for bus in buses:
            count = 0
            while i < len(passengers) and passengers[i] <= bus and count < capacity:
                if passengers[i] - 1 not in passenger_set:
                    arrive = passengers[i] - 1
                i += 1
                count += 1

            if count < capacity:  
                arrive = bus
                while arrive in passenger_set:
                    arrive -= 1

        return arrive