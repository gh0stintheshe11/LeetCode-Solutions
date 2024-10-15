class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import Counter
        MOD = 10**9 + 7
        
        count = Counter(arr)
        keys = sorted(count)
        n = len(keys)
        result = 0
        
        for i in range(n):
            x = keys[i]
            T = target - x
            j, k = i, n - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i < j < k:
                        result += count[x] * count[y] * count[z]
                    elif i == j < k:
                        result += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        result += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        result += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    j += 1
                    k -= 1
        
        return result % MOD