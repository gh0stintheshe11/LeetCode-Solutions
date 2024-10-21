class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        n = len(nums)
        m = len(changeIndices)

        def check(s, x):
            numz = nums.copy()
            down = [float('inf')] * n

            for j in range(s - x - 1):
                i = changeIndices[j] - 1

                if numz[i] > 1:
                    down[i] = min(down[i], j)

            proc = []
            wait = []

            for i in range(n):
                if down[i] == float('inf'):
                    proc.append(i)
                else:
                    wait.append(i)

            wait.sort(key=lambda i: down[i] - numz[i])

            for j in range(s):
                i = changeIndices[j] - 1

                if down[i] == j and numz[i] > 1:
                    numz[i] = 0
                    proc.append(i)
                    continue

                decremented = False

                while proc:
                    i = proc.pop()

                    if numz[i] < 0:
                        continue

                    numz[i] -= 1
                    decremented = True

                    if numz[i] > -1:
                        proc.append(i)

                    break

                if decremented:
                    continue

                while wait:
                    i = wait.pop()

                    if numz[i] < 1:
                        continue

                    numz[i] -= 1
                    decremented = True

                    if numz[i] > -1:
                        proc.append(i)

                    break

                if decremented:
                    continue

                return True

            return all(x == -1 for x in numz)

        l = 0
        r = m

        while l < r:
            s = (l + r) // 2

            if check(s, 0) or check(s, 1):
                r = s
            else:
                l = s + 1

        return r if (check(r, 0) or check(r, 1)) else -1