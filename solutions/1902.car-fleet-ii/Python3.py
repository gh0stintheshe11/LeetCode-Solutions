class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        res = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]

            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]

                if speed <= speed_j or (res[j] != -1 and (pos_j - pos) / (speed - speed_j) >= res[j]):
                    stack.pop()
                else:
                    break

            if stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                res[i] = (pos_j - pos) / (speed - speed_j)

            stack.append(i)

        return res