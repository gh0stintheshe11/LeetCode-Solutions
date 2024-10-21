class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def f(upper):
            upper = str(upper)

            @cache
            def free(index, curSum, parity):
                s = int(curSum)
                s %= k

                if index == 0:
                    return int(int(s == 0) and int(parity == 0))

                total = 0
                for i in range(10):
                    if i % 2 == 0:
                        total += free(index - 1, str(s) + str(i), parity + 1)
                    if i % 2 == 1:
                        total += free(index - 1, str(s) + str(i), parity - 1)
                
                return total

            @cache
            def constrained(index, curSum, parity):
                s = int(curSum)
                s %= k

                if index == N:
                    return int(int(s == 0) and int(parity == 0))

                total = 0
                char = int(upper[index])

                for j in range(char):
                    tmp = str(s) + str(j)
                    if j % 2 == 0:
                        total += free(N - (index + 1), tmp, parity + 1)
                    if j % 2 == 1:
                        total += free(N - (index + 1), tmp, parity - 1)

                if char % 2 == 0:
                    total += constrained(index + 1, str(s) + str(char), parity + 1)
                if char % 2 == 1:
                    total += constrained(index + 1, str(s) + str(char), parity - 1)

                return total

            N = len(upper)
            total = 0
            for i in range(1, N):
                for j in range(1, 10):
                    if j % 2 == 0:
                        total += free(i - 1, str(j), 1)
                    if j % 2 == 1:
                        total += free(i - 1, str(j), -1)
            
            char = int(upper[0])
            if char == 0:
                return 0

            for j in range(1, char):
                if j % 2 == 0:
                    total += free(N - 1, str(j), 1)
                else:
                    total += free(N - 1, str(j), -1)

            if char % 2 == 0:
                total += constrained(1, str(char), 1)

            if char % 2 == 1:
                total += constrained(1, str(char), -1)

            return total

        return f(high) - f(low - 1)