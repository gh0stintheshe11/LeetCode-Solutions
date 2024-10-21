from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def all_substrings(s):
            n = len(s)
            substrs = set()
            for length in range(1, n + 1):
                for start in range(n - length + 1):
                    substrs.add(s[start:start + length])
            return substrs

        n = len(arr)
        answers = [''] * n
        all_substrs = [all_substrings(arr[i]) for i in range(n)]

        for i in range(n):
            min_substring = None
            for substr in all_substrs[i]:
                unique = True
                for j in range(n):
                    if i != j and substr in all_substrs[j]:
                        unique = False
                        break
                if unique:
                    if min_substring is None or len(substr) < len(min_substring) or (len(substr) == len(min_substring) and substr < min_substring):
                        min_substring = substr
            answers[i] = min_substring if min_substring is not None else ''

        return answers