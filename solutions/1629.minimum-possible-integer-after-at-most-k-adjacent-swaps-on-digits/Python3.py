class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from sortedcontainers import SortedList

        n = len(num)
        sl = SortedList()
        result = []
        indices = [[] for _ in range(10)]

        for i, char in enumerate(num):
            indices[int(char)].append(i)
        
        for _ in range(n):
            for digit in range(10):
                if indices[digit]:
                    actual_index = indices[digit][0]
                    swaps_needed = actual_index - sl.bisect_left(actual_index)
                    if swaps_needed <= k:
                        k -= swaps_needed
                        result.append(str(digit))
                        sl.add(actual_index)
                        indices[digit].pop(0)
                        break
        
        return ''.join(result)