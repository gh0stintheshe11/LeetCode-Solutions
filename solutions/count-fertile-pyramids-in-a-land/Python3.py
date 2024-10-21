class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:

        def count() -> None:
            nonlocal ans
            prev_row = grid[0]

            for row in grid[1:]:
                curr_row = row[::]

                for j in range(1, len(grid[0]) - 1):

                    if curr_row[j] == 0: continue

                    curr_row[j] = min(prev_row[j - 1:j + 2])
                    ans += curr_row[j]
                    curr_row[j] += 1

                prev_row = curr_row

            return

        ans = 0
        count()
        grid = grid[::-1]
        count()

        return ans