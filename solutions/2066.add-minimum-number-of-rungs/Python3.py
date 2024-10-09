class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current_height = 0
        added_rungs = 0
        
        for rung in rungs:
            if rung - current_height > dist:
                added_rungs += (rung - current_height - 1) // dist
            current_height = rung
            
        return added_rungs