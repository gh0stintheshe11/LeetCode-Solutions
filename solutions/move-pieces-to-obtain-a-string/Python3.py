class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def filter_and_index(s):
            return [(c, i) for i, c in enumerate(s) if c != '_']

        start_filtered = filter_and_index(start)
        target_filtered = filter_and_index(target)

        if len(start_filtered) != len(target_filtered):
            return False

        for (c1, i1), (c2, i2) in zip(start_filtered, target_filtered):
            if c1 != c2:
                return False
            if c1 == 'L' and i1 < i2:
                return False
            if c1 == 'R' and i1 > i2:
                return False

        return True