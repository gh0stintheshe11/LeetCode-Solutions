class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from collections import defaultdict
        import bisect
        
        full_lakes = {}
        dry_days = []
        result = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full_lakes:
                    # We need to dry the lake before this day
                    day_to_dry = bisect.bisect_left(dry_days, full_lakes[lake])
                    if day_to_dry == len(dry_days):
                        return []  # No valid day to dry
                    # Replace the dry day with the lake to dry
                    result[dry_days.pop(day_to_dry)] = lake
                full_lakes[lake] = i
            else:
                dry_days.append(i)
        
        # Fill remaining dry days with any lake number, because they won't affect the result
        for day in dry_days:
            result[day] = 1
        
        return result