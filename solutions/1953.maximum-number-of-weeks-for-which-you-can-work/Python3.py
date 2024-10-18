class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        max_milestone = max(milestones)
        
        if max_milestone > total - max_milestone:
            return 2 * (total - max_milestone) + 1
        else:
            return total