class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length):
            mod = 2**63 - 1
            base = 26
            current_hash = 0
            for i in range(length):
                current_hash = (current_hash * base + nums[i]) % mod
            
            seen = {current_hash}
            base_len = pow(base, length, mod)
            
            for i in range(1, n - length + 1):
                current_hash = (current_hash * base - nums[i - 1] * base_len + nums[i + length - 1]) % mod
                if current_hash in seen:
                    return i
                seen.add(current_hash)
            return -1

        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        
        left, right = 1, n
        start = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            pos = search(mid)
            if pos != -1:
                start = pos
                left = mid + 1
            else:
                right = mid - 1
        
        return s[start:start + left - 1] if start != -1 else ""