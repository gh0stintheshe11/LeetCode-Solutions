class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        pt_indices = [None, None, None, None]
        min_int_sums = [float('inf'), float('inf')]
        min_int_diff = [float('inf'), float('inf')]
        max_int_sums = [float('-inf'), float('-inf')]
        max_int_diff = [float('-inf'), float('-inf')]
        answer = float('inf')
        for point_index, point in enumerate(points): 
            point_sum = point[0] + point[1]
            point_diff = point[0] - point[1]
            calc_map_0 = [point_sum, min_int_sums, 'lt', 0]
            calc_map_1 = [point_sum, max_int_sums, 'gt', 1]
            calc_map_2 = [point_diff, min_int_diff, 'lt', 2]
            calc_map_3 = [point_diff, max_int_diff, 'gt', 3]
            calc_maps = [calc_map_0, calc_map_1, calc_map_2, calc_map_3]
            for calc_map in calc_maps: 
                value = calc_map[0]
                target = calc_map[1]
                comparator_choice = calc_map[2]
                pt_index_current = calc_map[3]
                if comparator_choice == 'lt': 
                    if value < target[0]: 
                        pt_indices[pt_index_current] = point_index
                        target[1] = target[0]
                        target[0] = value 
                    elif value < target[1]:
                        target[1] = value
                    else: 
                        continue 
                else: 
                    if value > target[0]: 
                        pt_indices[pt_index_current] = point_index 
                        target[1] = target[0]
                        target[0] = value
                    elif value > target[1]: 
                        target[1] = value 
                    else: 
                        continue 

        for pt_index in pt_indices: 
            min_int_sum_val = min_int_sums[1] if pt_index == pt_indices[0] else min_int_sums[0]
            max_int_sum_val = max_int_sums[1] if pt_index == pt_indices[1] else max_int_sums[0]
            min_int_dif_val = min_int_diff[1] if pt_index == pt_indices[2] else min_int_diff[0]
            max_int_dif_val = max_int_diff[1] if pt_index == pt_indices[3] else max_int_diff[0]
            answer = min(answer, max(max_int_sum_val - min_int_sum_val, max_int_dif_val - min_int_dif_val))

        return answer