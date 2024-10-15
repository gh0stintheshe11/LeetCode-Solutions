class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        
        # Create a list of people who like each hat
        hat_to_people = [[] for _ in range(41)]
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_people[hat].append(person)
        
        # dp[mask][hat] means the number of ways to assign hats to people represented by mask using hats 1 to hat
        dp = [[0] * 41 for _ in range(1 << n)]
        dp[0][0] = 1
        
        for hat in range(1, 41):
            for mask in range(1 << n):
                dp[mask][hat] = dp[mask][hat - 1]
                for person in hat_to_people[hat]:
                    if mask & (1 << person):
                        dp[mask][hat] += dp[mask ^ (1 << person)][hat - 1]
                        dp[mask][hat] %= MOD
        
        return dp[(1 << n) - 1][40]