class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def check(length: int) -> bool:
            base, mod = 10**6, 2**63 - 1
            base_l = pow(base, length, mod)
            
            def get_hash(path):
                curr_hash = 0
                for i in range(length):
                    curr_hash = (curr_hash * base + path[i]) % mod
                hashes = {curr_hash}
                for i in range(length, len(path)):
                    curr_hash = (curr_hash * base - path[i - length] * base_l + path[i]) % mod
                    hashes.add(curr_hash)
                return hashes

            common_hashes = get_hash(paths[0])
            for path in paths[1:]:
                common_hashes &= get_hash(path)
                if not common_hashes:
                    return False
            return True

        left, right = 0, min(len(path) for path in paths)
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left