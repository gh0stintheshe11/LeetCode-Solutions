class Solution:
    def closestFair(self, n: int) -> int:
        def dfs(i):
            i, count = str(i), 0

            for char in i:
                if int(char) % 2 == 1:
                    count += 1
                else:
                    count -= 1

            return count == 0

        def func(n):
            total = 10**len(str(n))

            for i in range(len(str(n))//2):
                total += 10**i

            return total

        if len(str(n)) % 2 == 1:
            return func(n)

        for i in range(n, 10 * n):
            if len(str(i)) % 2 == 1:
                return func(i)

            if dfs(i):
                return i

        return -1