class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = 0
        k -= 1
        while k > 0:
            x = int(math.log(k, 2))
            count += operations[x]
            k -= 2 ** x
        return chr(ord('a') + count % 26)