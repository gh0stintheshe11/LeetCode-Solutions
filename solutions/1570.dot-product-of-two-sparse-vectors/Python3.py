from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_value_map = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # Iterate over the non-zero elements in this sparse vector
        for i, val in self.index_value_map.items():
            if i in vec.index_value_map:
                result += val * vec.index_value_map[i]
        return result