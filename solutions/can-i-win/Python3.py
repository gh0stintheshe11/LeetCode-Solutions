class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        
        memo = {}
        
        def can_win(choices, remaining):
            if choices[-1] >= remaining:
                return True
            key = tuple(choices)
            if key in memo:
                return memo[key]
            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i+1:], remaining - choices[i]):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        
        return can_win(list(range(1, maxChoosableInteger + 1)), desiredTotal)