class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        max_row_index = -1
        for index, row in enumerate(mat):
            count_ones = sum(row)
            if count_ones > max_ones:
                max_ones = count_ones
                max_row_index = index
        return [max_row_index, max_ones]