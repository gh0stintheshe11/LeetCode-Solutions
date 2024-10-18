class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        sequence_count = 0

        for roll in rolls:
            seen.add(roll)
            if len(seen) == k:
                sequence_count += 1
                seen.clear()

        return sequence_count + 1