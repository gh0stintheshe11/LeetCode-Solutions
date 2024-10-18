class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        memo = {}

        def is_valid_position(state, row):
            for j in range(n):
                if (state & (1 << j)) and seats[row][j] == '#':
                    return False
                if (state & (1 << j)) and (state & (1 << (j + 1))):
                    return False
            return True

        def max_students(row, prev_state):
            if row == m:
                return 0
            if (row, prev_state) in memo:
                return memo[(row, prev_state)]

            max_students_count = 0
            for state in range(1 << n):
                if is_valid_position(state, row):
                    valid_placement = True
                    for j in range(n):
                        if (state & (1 << j)):
                            if j > 0 and (prev_state & (1 << (j - 1))):
                                valid_placement = False
                            if j < n - 1 and (prev_state & (1 << (j + 1))):
                                valid_placement = False
                    if valid_placement:
                        max_students_count = max(
                            max_students_count,
                            bin(state).count('1') + max_students(row + 1, state)
                        )
            memo[(row, prev_state)] = max_students_count
            return max_students_count

        return max_students(0, 0)