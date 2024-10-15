class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        freq_map = defaultdict(int)
        
        for num in nums:
            freq_map[num] += 1

        max_freq = max(freq_map.values())
        
        result = [[] for _ in range(max_freq)]
        
        for num, count in freq_map.items():
            for i in range(count):
                result[i].append(num)
        
        return result