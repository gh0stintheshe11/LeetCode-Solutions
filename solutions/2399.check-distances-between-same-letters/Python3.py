class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_occurrence = [-1] * 26
        
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            if first_occurrence[index] == -1:
                first_occurrence[index] = i
            else:
                if i - first_occurrence[index] - 1 != distance[index]:
                    return False
        return True