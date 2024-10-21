class Solution:
    def reinitializePermutation(self, n: int) -> int:
        initial_perm = list(range(n))
        perm = initial_perm[:]
        count = 0
        
        while True:
            count += 1
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            perm = arr
            if perm == initial_perm:
                break
        
        return count