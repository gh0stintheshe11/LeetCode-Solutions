class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_positions = {'M': -1, 'P': -1, 'G': -1}
        total_garbage_time = 0
        
        # Calculate total garbage collection time and last positions of each garbage type
        for i, items in enumerate(garbage):
            total_garbage_time += len(items)
            for garbage_type in last_positions:
                if garbage_type in items:
                    last_positions[garbage_type] = i

        # Prepare prefix sum of travel times
        prefix_travel = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            prefix_travel[i + 1] = prefix_travel[i] + travel[i]
        
        # Add travel time for each garbage type based on its last collection position
        for garbage_type, last_pos in last_positions.items():
            if last_pos != -1:
                total_garbage_time += prefix_travel[last_pos]
        
        return total_garbage_time