class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        prefix_map = {0: 1}
        interesting_count = 0
        
        for num in nums:
            if num % modulo == k:
                prefix_count += 1
            current_mod = prefix_count % modulo
            target_mod = (current_mod - k + modulo) % modulo
            
            if target_mod in prefix_map:
                interesting_count += prefix_map[target_mod]
            
            if current_mod not in prefix_map:
                prefix_map[current_mod] = 0
            prefix_map[current_mod] += 1
            
        return interesting_count