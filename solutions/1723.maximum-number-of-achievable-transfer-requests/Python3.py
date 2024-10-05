from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0
        total_requests = len(requests)
        
        # Iterate over all possible subsets of requests
        for mask in range(1 << total_requests):
            net_change = [0] * n
            count = 0
            
            for i in range(total_requests):
                if mask & (1 << i):
                    from_building, to_building = requests[i]
                    net_change[from_building] -= 1
                    net_change[to_building] += 1
                    count += 1
            
            # Check if the current subset is valid
            if all(change == 0 for change in net_change):
                max_requests = max(max_requests, count)
        
        return max_requests