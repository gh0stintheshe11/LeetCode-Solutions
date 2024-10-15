class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] != '0':
            return False

        queue = [0]  # to store reachable indices
        farthest = 0  # the farthest index reached so far

        for i in range(1, n):
            # clear indices in the queue that are not useful anymore (i.e., they lead to jumps out of range)
            # because if `i` is already greater than farthest + maxJump, we can stop checking older indices
            if queue and queue[0] < i - maxJump:
                queue.pop(0)

            # check if `i` can be reached
            if i >= minJump and s[i] == '0' and queue and queue[0] <= i - minJump:
                if i == n - 1:
                    return True
                queue.append(i)

        return False