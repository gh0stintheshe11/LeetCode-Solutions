class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        
        result = []
        current_even = 2
        while finalSum >= current_even:
            result.append(current_even)
            finalSum -= current_even
            current_even += 2
        
        if finalSum > 0:
            result[-1] += finalSum
        
        return result