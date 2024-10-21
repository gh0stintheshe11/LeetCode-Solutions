class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.score = 0
        self.snake = collections.deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

    def move(self, direction: str) -> int:
        current_head = self.snake[0]
        delta_row, delta_col = self.directions[direction]
        new_head = (current_head[0] + delta_row, current_head[1] + delta_col)

        if (new_head[0] < 0 or new_head[0] >= self.height or
                new_head[1] < 0 or new_head[1] >= self.width or
                (new_head in self.snake_set and new_head != self.snake[-1])):
            return -1

        if self.food_index < len(self.food) and list(new_head) == self.food[self.food_index]:
            self.food_index += 1
            self.score += 1
        else:
            removed_tail = self.snake.pop()
            self.snake_set.remove(removed_tail)

        self.snake.appendleft(new_head)
        self.snake_set.add(new_head)

        return self.score