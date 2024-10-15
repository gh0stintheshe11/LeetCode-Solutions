from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        current = set()
        for num in arr:
            current = {num | x for x in current} | {num}
            res.update(current)
        return len(res)