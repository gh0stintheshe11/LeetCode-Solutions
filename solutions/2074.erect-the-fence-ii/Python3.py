import math
from typing import List
import random

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        def circle_from_2_points(p1, p2):
            center = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            radius = dist(p1, center)
            return center + [radius]

        def circle_from_3_points(p1, p2, p3):
            ax, ay = p1
            bx, by = p2
            cx, cy = p3
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                return [0, 0, float('inf')]
            ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
            uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
            center = [ux, uy]
            radius = dist(center, p1)
            return center + [radius]

        def is_inside_circle(p, c):
            return dist(p, c[:2]) <= c[2] + 1e-9

        def welzl(points, r=[], depth=0):
            if not points or len(r) == 3:
                if len(r) == 0:
                    return [0, 0, 0]
                elif len(r) == 1:
                    return r[0] + [0]
                elif len(r) == 2:
                    return circle_from_2_points(r[0], r[1])
                else:
                    return circle_from_3_points(r[0], r[1], r[2])

            p = points.pop()
            c = welzl(points, r, depth + 1)

            if is_inside_circle(p, c):
                points.append(p)
                return c

            new_r = r + [p]
            result = welzl(points, new_r, depth + 1)
            points.append(p)
            return result

        random.shuffle(trees)
        circle = welzl(trees)
        return circle