class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def rabin_karp(pattern, s):
            # Rabin-Karp String matching
            base = 256
            mod = 10 ** 9 + 7
            target_hash = 0
            res = []
            if len(s) < len(pattern): return []
            for i in range(len(pattern)):
                target_hash = (target_hash * base + ord(pattern[i])) % mod
            
            curr_hash = 0
            for i in range(len(pattern)):
                curr_hash = (curr_hash * base + ord(s[i])) % mod
            if curr_hash == target_hash: res.append(0)

            high_base_pow = pow(base, len(pattern)-1, mod)

            l = 0
            r = len(pattern) - 1
            while r+1 < len(s):
                curr_hash = (curr_hash - ord(s[l]) * high_base_pow) % mod
                curr_hash = (curr_hash * base + ord(s[r+1])) % mod
                if curr_hash < 0: curr_hash += mod
    
                if curr_hash == target_hash:
                    res.append(l+1)
                l += 1
                r += 1

            return res

        def binary_search(target, nums, k):
            lo = 0 
            hi = len(nums) - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                condition = abs(target - nums[mid])
                if condition <= k: return True
                elif nums[mid] > target: hi = mid - 1
                else: lo = mid + 1
            return False
            
        A = rabin_karp(a, s)
        B = rabin_karp(b, s)

        res = []

        for value in A:
            if binary_search(value, B, k):
                res.append(value)

        return res