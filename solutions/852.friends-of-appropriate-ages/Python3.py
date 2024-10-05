from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_counts = [0] * 121
        for age in ages:
            age_counts[age] += 1

        requests = 0
        for x in range(121):
            if age_counts[x] == 0:
                continue
            for y in range(121):
                if age_counts[y] == 0:
                    continue
                if y <= 0.5 * x + 7:
                    continue
                if y > x:
                    continue
                if y > 100 and x < 100:
                    continue
                requests += age_counts[x] * (age_counts[y] if x != y else age_counts[y] - 1)
        
        return requests