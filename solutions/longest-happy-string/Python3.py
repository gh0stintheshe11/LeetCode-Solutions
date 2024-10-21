class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        from heapq import heappush, heappop
        
        max_heap = []
        if a > 0:
            heappush(max_heap, (-a, 'a'))
        if b > 0:
            heappush(max_heap, (-b, 'b'))
        if c > 0:
            heappush(max_heap, (-c, 'c'))

        result = []

        while max_heap:
            first_count, first_char = heappop(max_heap)
            if result[-2:] == [first_char, first_char]:
                if not max_heap:
                    break
                second_count, second_char = heappop(max_heap)
                result.append(second_char)
                second_count += 1
                if second_count < 0:
                    heappush(max_heap, (second_count, second_char))
                heappush(max_heap, (first_count, first_char))
            else:
                result.append(first_char)
                first_count += 1
                if first_count < 0:
                    heappush(max_heap, (first_count, first_char))

        return "".join(result)