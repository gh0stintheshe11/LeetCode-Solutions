from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])  # (position, speed)
        visited = set((0, 1))
        steps = 0

        while queue:
            for _ in range(len(queue)):
                position, speed = queue.popleft()

                if position == target:
                    return steps

                # Accelerate
                new_position = position + speed
                new_speed = speed * 2
                if (new_position, new_speed) not in visited and 0 <= new_position <= 2 * target:
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed))

                # Reverse
                new_speed = -1 if speed > 0 else 1
                if (position, new_speed) not in visited:
                    visited.add((position, new_speed))
                    queue.append((position, new_speed))

            steps += 1