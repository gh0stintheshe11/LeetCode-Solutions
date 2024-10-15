class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common = [0] * n
        seen_A, seen_B = set(), set()
        
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            common_count = len(seen_A.intersection(seen_B))
            prefix_common[i] = common_count
        
        return prefix_common