class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        sorted_arr = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_arr)}
        
        return [rank_map[num] for num in arr]