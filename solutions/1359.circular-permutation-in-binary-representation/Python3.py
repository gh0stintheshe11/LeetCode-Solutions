class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_code_sequence = [i ^ (i >> 1) for i in range(1 << n)]
        start_index = gray_code_sequence.index(start)
        return gray_code_sequence[start_index:] + gray_code_sequence[:start_index]