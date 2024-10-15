class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict
        
        # Dictionary to hold the set of unique active minutes for each user
        user_minutes = defaultdict(set)
        
        # Populate the dictionary with the user's actions
        for user_id, time in logs:
            user_minutes[user_id].add(time)
        
        # Create an array to count occurrences of each UAM
        uam_count = [0] * k
        
        # Count the UAMs for each user
        for minutes in user_minutes.values():
            uam = len(minutes)
            if uam <= k:
                uam_count[uam - 1] += 1
        
        return uam_count