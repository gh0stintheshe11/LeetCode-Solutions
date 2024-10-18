from typing import List

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        count = 0
        for x in a:
            for y in b:
                for z in c:
                    if bin(x ^ y ^ z).count('1') % 2 == 0:
                        count += 1
        return count