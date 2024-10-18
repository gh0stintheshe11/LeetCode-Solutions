class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        b_count = 0
        min_deletions = a_count
        
        for char in s:
            if char == 'a':
                a_count -= 1
            else:
                b_count += 1
            min_deletions = min(min_deletions, b_count + a_count)
        
        return min_deletions