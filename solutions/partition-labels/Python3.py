class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: index for index, char in enumerate(s)}
        start, end = 0, 0
        partitions = []
        
        for index, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if index == end:
                partitions.append(end - start + 1)
                start = index + 1
        
        return partitions