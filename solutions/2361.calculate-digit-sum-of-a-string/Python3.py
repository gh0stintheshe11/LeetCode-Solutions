class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []
            for start in range(0, len(s), k):
                group = s[start:start + k]
                sum_group = sum(int(char) for char in group)
                new_s.append(str(sum_group))
            s = ''.join(new_s)
        return s