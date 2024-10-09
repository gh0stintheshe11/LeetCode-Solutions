class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        count0 = s.count('0')
        count1 = n - count0
        
        if abs(count0 - count1) > 1:
            return -1
        
        def count_mismatches(alternate):
            mismatches = 0
            for i in range(n):
                if s[i] != alternate[i]:
                    mismatches += 1
            return mismatches // 2
        
        if count0 == count1:
            pattern1 = '01' * (n // 2) + ('0' if n % 2 else '')
            pattern2 = '10' * (n // 2) + ('1' if n % 2 else '')
            return min(count_mismatches(pattern1), count_mismatches(pattern2))
        elif count0 > count1:
            pattern = '01' * (n // 2) + ('0' if n % 2 else '')
            return count_mismatches(pattern)
        else:
            pattern = '10' * (n // 2) + ('1' if n % 2 else '')
            return count_mismatches(pattern)