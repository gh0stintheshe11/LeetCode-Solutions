class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        result = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60  # This handles the case where t % 60 == 0
            result += count[complement]
            count[remainder] += 1
        return result