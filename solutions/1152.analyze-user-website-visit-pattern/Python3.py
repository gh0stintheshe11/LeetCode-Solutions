from collections import defaultdict, Counter
from itertools import combinations
from typing import List, Tuple

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Gather and sort the user data by timestamps
        user_data = sorted(zip(timestamp, username, website))
        
        # Step 2: Organize websites each user visits in chronological order
        user_to_websites = defaultdict(list)
        for time, user, web in user_data:
            user_to_websites[user].append(web)

        # Step 3: Count 3-sequence patterns visited by users
        patterns = Counter()
        for websites in user_to_websites.values():
            combs = set(combinations(websites, 3))
            patterns.update(combs)
        
        # Step 4: Find the max pattern based on the given criteria
        max_pattern = max(sorted(patterns), key=lambda pattern: patterns[pattern])
        
        return list(max_pattern)