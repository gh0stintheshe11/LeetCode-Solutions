from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_count = {}
        distinct_colors = 0
        result = []

        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                if color_count[old_color] == 1:
                    distinct_colors -= 1
                color_count[old_color] -= 1
            
            ball_to_color[ball] = color

            if color not in color_count or color_count[color] == 0:
                distinct_colors += 1
            
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1

            result.append(distinct_colors)

        return result