import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        c1 = [0] * (n + 1)

        for i in range(1, n + 1):
            c1[i] = c1[i - 1] + (1 if s[i - 1] == '1' else 0)

        total_ones = c1[-1]

        next_zero = [0] * n

        curr_zero_pos = n

        for i in range(n - 1, -1, -1):
            next_zero[i] = curr_zero_pos
            if s[i] == '0':
                curr_zero_pos = i

        total = 0

        for i in range(n):
            curr_zero_count = (1 if s[i] == '0' else 0)
            curr_zero_pos = i
            next_zero_pos = next_zero[i]

            for cz in range(201):

                if (total_ones - c1[i]) < curr_zero_count**2:
                    break

                curr_valid_one_pos = bisect.bisect_left(
                    c1,
                    c1[i] + curr_zero_count**2,
                    curr_zero_pos + 1,
                    next_zero_pos + 1
                )

                total += next_zero_pos + 1 - curr_valid_one_pos

                if next_zero_pos == n:
                    break
                curr_zero_pos = next_zero_pos
                next_zero_pos = next_zero[curr_zero_pos]
                curr_zero_count += 1

        return total