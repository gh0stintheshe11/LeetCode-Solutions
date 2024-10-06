class Solution:
    def houseOfCards(self, n: int) -> int:
        def countWays(remaining_cards, prev_k):
            if remaining_cards == 0:
                return 1
            if remaining_cards < 0 or prev_k == 0:
                return 0

            # Using memoization to store previously computed results
            if memo[remaining_cards][prev_k] != -1:
                return memo[remaining_cards][prev_k]

            ways = 0
            for k in range(1, prev_k):
                cards_needed = 3 * k - 1
                if remaining_cards >= cards_needed:
                    ways += countWays(remaining_cards - cards_needed, k)
            
            memo[remaining_cards][prev_k] = ways
            return ways
        
        # Using memoization to store previous results, initialize with -1
        memo = [[-1] * (n + 1) for _ in range(n + 1)]
        
        return countWays(n, n)