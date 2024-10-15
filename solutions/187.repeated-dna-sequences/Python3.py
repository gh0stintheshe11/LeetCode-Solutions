from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = {}
        result = []
        
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in sequence_count:
                sequence_count[sequence] += 1
            else:
                sequence_count[sequence] = 1
                
        for sequence, count in sequence_count.items():
            if count > 1:
                result.append(sequence)
                
        return result