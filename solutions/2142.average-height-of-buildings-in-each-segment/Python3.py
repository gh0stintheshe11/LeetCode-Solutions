class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end, height in buildings:
            events.append((start, height))
            events.append((end, -height))
        
        events.sort()

        current_sum = 0
        current_count = 0
        last_position = 0
        result = []

        for position, height_change in events:
            if current_count > 0 and position > last_position:
                avg_height = current_sum // current_count
                if result and result[-1][1] == last_position and result[-1][2] == avg_height:
                    result[-1][1] = position
                else:
                    result.append([last_position, position, avg_height])

            current_sum += height_change
            if height_change > 0:
                current_count += 1
            else:
                current_count -= 1

            last_position = position

        return result