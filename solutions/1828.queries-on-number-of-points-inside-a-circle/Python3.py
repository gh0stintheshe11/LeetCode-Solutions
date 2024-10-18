class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for xj, yj, rj in queries:
            count = 0
            for xi, yi in points:
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2:
                    count += 1
            answer.append(count)
        return answer