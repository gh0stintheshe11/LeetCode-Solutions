class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries) -> int:
        counts = {'0': 0, '1': 0}

        i = 0
        j = 0
        n = len(s)

        starts = list(range(n))
        ends = [0] * n

        while j < n:
            c = s[j]
            counts[c] += 1

            while counts['0'] > k and counts['1'] > k:
                ends[i] = j - 1
                counts[s[i]] -= 1
                i += 1
            
            starts[j] = i
            j += 1
        while i < n:
            ends[i] = j - 1
            counts[s[i]] -= 1
            i += 1
        
        col_0s = [0] * n
        row_0s = [0] * n

        starts_before = [0] * (n + 1)

        for i in range(n):
            starts_at_i = ends[i] - i + 1
            starts_before[i + 1] = starts_before[i] + starts_at_i
            row_0s[i] = (n - i) - starts_at_i
            col_0s[i] = starts[i]
        
        left_empty = [0] * (n + 1)
        down_empty = [0] * (n + 1)
        for i in range(n):
            left_empty[i] = left_empty[i - 1] + col_0s[i]
        all_empty = left_empty[n - 1]
        down_empty[0] = all_empty
        for i in range(1, n):
            down_empty[i] = down_empty[i - 1] - row_0s[i - 1]

        def query(i, j):
            n = j - i + 1
            T = n * (n + 1) // 2
            if starts[j] <= i:
                return T
            if i > 0:
                B = starts_before[i]
                BF = (j + 1 + j + 2 - i) * i // 2
                F = BF - B
            else:
                F = 0
            EF = left_empty[j]
            E = EF - F
            return T - E
            
        ans = []
        for li, ri in queries:
            ans.append(query(li, ri))

        return ans