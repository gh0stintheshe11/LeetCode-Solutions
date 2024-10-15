class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(index):
            if index == size:
                return True
            if sequence[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if num_used[num]:
                    continue
                if num == 1:
                    sequence[index] = 1
                    num_used[1] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    num_used[1] = False
                else:
                    if index + num >= size or sequence[index + num] != 0:
                        continue
                    sequence[index] = num
                    sequence[index + num] = num
                    num_used[num] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    sequence[index + num] = 0
                    num_used[num] = False
            return False

        size = 2 * n - 1
        sequence = [0] * size
        num_used = [False] * (n + 1)
        backtrack(0)
        return sequence