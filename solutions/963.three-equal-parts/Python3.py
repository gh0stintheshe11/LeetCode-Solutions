class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = sum(arr)
        if ones % 3 != 0:
            return [-1, -1]
        if ones == 0:
            return [0, len(arr) - 1]
        
        target_ones_per_part = ones // 3
        first, second, third, ones_count = -1, -1, -1, 0
        
        for i, bit in enumerate(arr):
            if bit == 1:
                if ones_count % target_ones_per_part == 0:
                    if ones_count == 0:
                        first = i
                    elif ones_count == target_ones_per_part:
                        second = i
                    elif ones_count == 2 * target_ones_per_part:
                        third = i
                ones_count += 1
        
        while third < len(arr) and arr[first] == arr[second] and arr[first] == arr[third]:
            first += 1
            second += 1
            third += 1
        
        if third == len(arr):
            return [first - 1, second]
        
        return [-1, -1]