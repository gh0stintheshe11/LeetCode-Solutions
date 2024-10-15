class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        from collections import Counter
        
        m, n = len(mat), len(mat[0])
        frequency = Counter()
        
        for row in mat:
            for num in row:
                frequency[num] += 1
        
        for num in sorted(frequency):
            if frequency[num] == m:
                return num
                
        return -1