class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}
        
        def can_player_win(state):
            if state in memo:
                return memo[state]
            
            for i in range(len(state) - 1):
                if state[i:i+2] == '++':
                    next_state = state[:i] + '--' + state[i+2:]
                    if not can_player_win(next_state):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False
        
        return can_player_win(currentState)