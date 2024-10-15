class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = float('inf')
        valid = set()
        
        for num in arr:
            new_valid = {num}
            
            for v in valid:
                new_valid.add(v & num)
            
            for v in new_valid:
                res = min(res, abs(v - target))
                
            valid = new_valid
        
        return res