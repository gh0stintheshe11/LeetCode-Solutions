class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n - k))
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(n - k + i // 2)
            else:
                result.append(n - i // 2)
        return result