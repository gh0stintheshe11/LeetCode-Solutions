class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        for size in range(len(arr), 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    flip(max_index)
                    result.append(max_index + 1)
                flip(size - 1)
                result.append(size)
                
        return result