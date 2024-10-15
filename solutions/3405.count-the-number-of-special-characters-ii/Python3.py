class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper_idx = {}
        last_lower_idx = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower_idx[c] = i
            else:
                if c not in first_upper_idx:
                    first_upper_idx[c] = i

        special_count = 0

        for c in last_lower_idx:
            upper_c = c.upper()
            if upper_c in first_upper_idx and last_lower_idx[c] < first_upper_idx[upper_c]:
                special_count += 1
        
        return special_count