class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        from collections import defaultdict
        
        player_color_count = defaultdict(lambda: defaultdict(int))
        
        for player, color in pick:
            player_color_count[player][color] += 1
        
        winning_count = 0
        
        for player in range(n):
            if any(count > player for count in player_color_count[player].values()):
                winning_count += 1
        
        return winning_count